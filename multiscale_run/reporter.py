from pathlib import Path

import h5py
import numpy as np

from multiscale_run import utils


class MsrReporterException(Exception):
    pass


class MsrReporter:
    """A class for reporting multiscale simulation data."""

    def __init__(self, config, gids: list[int], t_unit="ms"):
        """Initializes the MsrReporter instance.

        Args:
            config (MsrConfig): Configuration argument.
            gids : List of gids.
            n_bf_segs: number of bloodflow segments.
            t_unit (optional): Time unit. Defaults to "ms".
        """

        self.config = config
        self.t_unit = t_unit

        self._init_offsets(gids)

    def _init_offsets(self, gids: list[int]):
        """Initializes offsets for the gids.

        Args:
            gids: List of gids.
        """
        self.all_gids = utils.comm().gather(gids, root=0)
        ps = []
        if utils.rank0():
            ps = [0, *np.cumsum([len(i) for i in self.all_gids[:-1]])]
            self.all_gids = [j for i in self.all_gids for j in i]

        self.offset = utils.comm().scatter(ps, root=0)
        self.gid2pos = {gid: idx + self.offset for idx, gid in enumerate(gids)}

    @property
    def _data_loc(self):
        """Returns the data location string.

        Returns
            str: A string representing the data location within the HDF5 file.
        """
        return f"/report/{self.config.multiscale_run.preprocessor.node_sets.neuron_population_name}"

    def _file_path(self, title, rep, is_post_adv=False):
        file_name = Path(rep.file_name if "file_name" in rep else title).with_suffix('.h5')
        if is_post_adv:
            file_name = file_name.with_stem(f"{file_name.stem}_after_adv")
        
        return self.config.config_path.parent / self.config.output.output_dir / file_name


    def _init_file(self, title, rep, dt, is_post_adv):
        """ TODO
        """

        sim_end = self.config.run.tstop
        # timesteps generates a vector like [1, 2, 3, ..., n]. We also have a recording at t=0.
        # Thus, we need n+1 rows
        nrows = len(utils.timesteps(sim_end, dt))

        
        idxs = self.all_gids
        path = self._file_path(title, rep, is_post_adv)
        path.parent.mkdir(parents=True, exist_ok=True)
        with h5py.File(str(path), "w") as file:
            base_group = file.create_group(self._data_loc)
            data = np.zeros((nrows, len(idxs)), dtype=np.float32)
            data_dataset = base_group.create_dataset("data", data=data)
            data_dataset.attrs["units"] = rep.get("unit", '')
            mapping_group = base_group.create_group("mapping")
            data = np.array(idxs, dtype=np.uint64)
            mapping_group.create_dataset("node_ids", data=data)
            tvec = [dt, sim_end+dt, dt] if is_post_adv else [0, sim_end, dt]
            data = np.array(tvec, dtype=np.float64)
            time_dataset = mapping_group.create_dataset("time", data=data)
            time_dataset.attrs["units"] = self.t_unit

    def pick_config_reports_section(self, simulator):
        return self.config.reports if simulator == "neurodamus" else self.config.multiscale_run[simulator].reports

    def init_files(self, simulator: str, dt: float, is_post_adv):
        """Initializes files for reporting."""
        if utils.rank0():
            for title, rep in self.pick_config_reports_section(simulator).items():
                self._init_file(title, rep, dt, is_post_adv)

        utils.comm().Barrier()

    def record(self, idt: int, simulator: object, gids: list[int], is_post_adv: bool):
        """Records simulation data.

        Args:
            idt: time step index of the current manager.
            manager_name: current manager.
            managers: dict of managers
            TODO
        """

        for title, rep in self.pick_config_reports_section(simulator.name).items():

            path = self._file_path(title, rep, is_post_adv=is_post_adv)

            idxs = np.array(
                [self.gid2pos[gid] for gid in gids]
            )
            with h5py.File(path, "a", driver="mpio", comm=utils.comm()) as f:
                self._save_vals(simulator, rep, f, idt, idxs)

    def _save_vals(self, manager, rep, f, idt, idxs):
        dataset = f[f"{self._data_loc}/data"]

        if "src_get_func" in rep:
            vals = np.array(
                getattr(manager, rep.src_get_func)(**rep.get("src_get_kwargs",{})),
                dtype=np.float64,
            )
        else:
            vals = np.array(manager.get_compartment_report_var(rep.variable_name))

        if not len(vals):
            return

        dataset[int(idt), idxs] = vals
