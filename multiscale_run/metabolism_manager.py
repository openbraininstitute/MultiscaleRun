import enum
import logging

import libsonata
import numpy as np

from . import config, utils

from scipy.integrate import solve_ivp

from .metabolism import model, constants, initial_conditions, indexes


class MsrMetabManagerException(Exception):
    """Generic Metabolism Manager Exception"""


class MsrExcludeNeuronException(Exception):
    """This error should be recoverable. We just want to kick the neuron out
    of the simulation because it is misbehaving
    """


class MsrAbortSimulationException(Exception):
    """This error should not be recoverable. Something went very wrong and continuing the simulation is meaningless"""


class MsrMetabolismManager:
    """Wrapper to manage the metabolism model"""

    errors = {
        "abort_simulation": MsrAbortSimulationException,
        "exclude_neuron": MsrExcludeNeuronException,
    }

    def __init__(self, config, neuron_pop_name: str, raw_gids: list[int]):
        """Initialize the MsrMetabolismManager.

        Args:
            config: The configuration for the metabolism manager.
            main: An instance of the main class.
            neuron_pop_name: The name of the neuron population.
            gids: list of cells to reset.
        """
        self.config = config

        self.vm = None  # read/write values for metab
        self.parameters = None  # read values for metab
        self.tspan_m = (-1, -1)
        self.neuron_node_pop = libsonata.CircuitConfig.from_file(
            str(self.config.config_path.parent / self.config.network)
        ).node_population(neuron_pop_name)
        self.raw_gids = raw_gids
        self.reset()

    def get_error(self, key: str):
        try:
            return self.errors[key]
        except KeyError as e:
            raise config.MsrConfigException(
                f"The error `{key}` does not exist in the config file: '{self.config.config_path}' or its logic is not implemented in metabolism. Possible values: {', '.join(self.errors)}"
            ) from e

    @property
    def ngids(self):
        """Gid number"""
        return len(self.raw_gids)
    
    @staticmethod
    def _strIdx2idx(idx_type, idxs):
        """Convert string index to actual index based on PIdx or UIdx"""
        if not isinstance(idxs, list):
            return getattr(idx_type, idxs)
        return [getattr(idx_type, i) for i in idxs]

    def set_parameters_idxs(self, vals: list[float], idxs: list[str] | str):
        """Set one or more parameters slices equal to the vals list"""
        if not isinstance(idxs, list):
            idxs = [idxs]
        idxs = self._strIdx2idx(indexes.PIdx, idxs)
        for idx in idxs:
            self.parameters[:, idx] = vals

    def set_vm_idxs(self, vals, idxs: list[str] | str):
        """Set one or more vm slices equal to the vals list"""
        if not isinstance(idxs, list):
            idxs = [idxs]
        idxs = self._strIdx2idx(indexes.UIdx, idxs)
        for idx in idxs:
            self.vm[:, idx] = vals

    def get_parameters_idx(self, idx: str):
        """Get parameters slice"""
        idx = self._strIdx2idx(indexes.PIdx, idx)
        return self.parameters[:, idx]

    def get_vm_idx(self, idx: str):
        """Get vm slice"""
        idx = self._strIdx2idx(indexes.UIdx, idx)
        return self.vm[:, idx]

    def alive_gids(self):
        """Convenience function to report which gids are still alive.

        All the gids present are still alive.
        """
        return [1] * self.parameters.shape[0]

    @utils.logs_decorator
    def _advance_gid(self, igid: int, i_metab: int, failed_cells: list[str]):
        """Advance metabolism simulation for gid: gids[igid] using Python.

        Args:
            igid: Index of the gid.
            i_metab: metabolism, time step counter.
            failed_cells: List of errors for the failed cells.
                Cells that are alive have `None` as value here.
        Raises:
            MsrMetabManagerException: If solver fails.
        """

        metab_dt = self.config.metabolism_dt
        tspan_m = (
            1e-3 * float(i_metab) * metab_dt,
            1e-3 * (float(i_metab) + 1.0) * metab_dt,
        )

        u0 = self.vm[igid, :]
        p = self.parameters[igid, :]

        try:
            logging.info(f"   solve ODE problem {igid}/{self.ngids}")

            # solve_ivp expects a function f(t, u)
            sol = solve_ivp(
                lambda t, u: model.compute_du(u, p, t),
                tspan_m,
                u0,
                vectorized=False,
                **self.config.multiscale_run.metabolism.solver_kwargs
            )

            logging.info("   /solve ODE problem")

            if not sol.success:
                utils.rank_print(f" !!! solver failed: {sol.message}")
                failed_cells[igid] = f"solver failed: {sol.message}"
            else:
                self.vm[igid, :] = sol.y[:, -1]

        except Exception as e:
            failed_cells[igid] = f"solver failed: {str(e)}"
            raise e

    @utils.logs_decorator
    def advance(self, i_metab: int, failed_cells: list) -> None:
        """Advance metabolism simulation

        Already failed cells are skipped.

        Args:
            i_metab: metabolism, time step counter.
            failed_cells: List of errors for the failed cells. Cells that are alive have `None` as value here.
        """
        for igid, err in enumerate(failed_cells):
            if err is not None:
                continue

            self._advance_gid(igid=igid, i_metab=i_metab, failed_cells=failed_cells)

    def _get_GLY_a_and_mito_vol_frac(self, raw_gid: int):
        """Get glycogen (GLY_a) and mitochondrial volume fraction.

        This method calculates glycogen (GLY_a) and mitochondrial volume fraction for a given neuron based on its layer.

        Args:
            raw_gid: 1-based raw gid (no offsets). GID: The Global ID of the neuron.

        Returns:
            a tuple (glycogen, mito_volume_fraction) where glycogen is
            the calculated glycogen value, and mito_volume_fraction is
            the calculated mitochondrial volume fraction.
        """
        # layer_idx: layers are 1-based while python vectors are 0-based
        layer_idx = int(self.neuron_node_pop.get_attribute("layer", raw_gid)) - 1
        glycogen_au = np.array(constants.Glycogen.au)
        mito_volume_fraction = np.array(
            constants.GeneralConstants.mito_volume_fraction
        )
        glycogen_scaled = glycogen_au * (14.0 / max(glycogen_au))
        mito_volume_fraction_scaled = mito_volume_fraction * (1.0 / max(mito_volume_fraction))
        return (
            glycogen_scaled[layer_idx],
            mito_volume_fraction_scaled[layer_idx],
        )


    @utils.logs_decorator
    def reset(self):
        """Reset the parameters and initial conditions for metabolic simulation.
        """
        self.reset_constants()
        self.reset_u0()
        self.reset_parameters()
        
    def reset_u0(self):
        metab_conf = self.config.multiscale_run.metabolism
        u0 = initial_conditions.make_u0()
        if "u0" in metab_conf:
            initial_conditions.override(u0, indexes.UIdx, metab_conf.u0)
        self.vm = np.tile(u0, (self.ngids, 1))

    def reset_parameters(self):
        metab_conf = self.config.multiscale_run.metabolism
        p0 = initial_conditions.make_parameters()
        if "parameters" in metab_conf:
            initial_conditions.override(p0, indexes.PIdx, metab_conf.parameters)
        self.parameters = np.tile(p0, (self.ngids, 1))
        # auto-override if not specifically stated in the conf
        if "mito_scale" not in metab_conf.parameters:
            self.parameters[:, indexes.PIdx.mito_scale] = [
                self._get_GLY_a_and_mito_vol_frac(c_gid)[1] for c_gid in self.raw_gids
            ]

    def reset_constants(self):
        metab_conf = self.config.multiscale_run.metabolism
        for cls_name, fields in metab_conf.constants.items():
            # Will throw if class doesn't exist
            cls = getattr(constants, cls_name)  

            # Get the allowed dataclass fields
            if not hasattr(cls, "__dataclass_fields__"):
                raise TypeError(f"{cls_name} is not a dataclass")

            allowed_keys = cls.__dataclass_fields__.keys()

            for key, value in fields.items():
                if key not in allowed_keys:
                    raise AttributeError(
                        f"{cls_name} has no attribute '{key}'. Available keys: {list(allowed_keys)}"
                    )
                if isinstance(value, list):
                    value = tuple(value)
                setattr(cls, key, value)

    def _check_input(self, v, conf, input_type, input_name, msg, failed_cells):

        for igid in range(self.ngids):
            if failed_cells[igid] is not None:
                continue
            idx = getattr(input_type, input_name)
            kwargs = conf.get("kwargs", {})
            err = self.get_error(conf.get("response", "abort_simulation"))
            gid = self.raw_gids[igid]
            msg += f".{input_name} (gid: {gid}) ({idx}): "
            for igid in range(self.ngids):
                if failed_cells[igid] is not None:
                    continue
                try:
                    utils.check_value(v=v[igid, idx], **kwargs, err=err, msg=msg)
                except MsrExcludeNeuronException as e:
                    failed_cells[igid] = str(e)


    @utils.logs_decorator
    def check_inputs(self, failed_cells: list[str]) -> None:
        metab_conf = self.config.multiscale_run.metabolism
        if "checks" not in metab_conf:
            return
        if "parameters" in metab_conf.checks:
            for parameter_name, conf in metab_conf.checks.parameters.items():
                    self._check_input(v=self.parameters, input_type=indexes.PIdx, input_name=parameter_name, conf=conf, msg="paramter", failed_cells=failed_cells)

        if "vm" in metab_conf.checks:
            for vm_name, conf in metab_conf.checks.vm.items():
                    self._check_input(v=self.vm, input_type=indexes.UIdx, input_name=vm_name, conf=conf, msg="vm", failed_cells=failed_cells)
