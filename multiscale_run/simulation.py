"""This module provides an API to instantiate, init,
and run simulations. It manipulates the "manager" classes
and orchestrate the different models and pass data between
them to perform the simulation
"""

import functools
import logging

from . import utils


def _run_once(f):
    """Decorator to ensure a function is called only once."""

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


class MsrSimulation:
    def __init__(self, base_path=None):
        self._base_path = base_path

    def main(self):
        self.compute()

    @staticmethod
    def stats():
        """Get some stats from a simulation"""
        from multiscale_run import neurodamus_manager

        neurodamus_manager.MsrNeurodamusManager.stats()

    @_run_once
    def warmup(self):
        """Instantiate the simulators in the proper and sensitive order"""
        logging.info("warmup simulators...")
        # this needs to be before "import neurodamus" and before MPI4PY otherwise mpi hangs

        from neuron import h

        h.nrnmpi_init()

        import neurodamus  # noqa: F401

        # steps_manager should go before preprocessor until https://github.com/CNS-OIST/HBP_STEPS/issues/1166 is solved
        from multiscale_run import (
            bloodflow_manager,  # noqa: F401
            connection_manager,
            metabolism_manager,
            neurodamus_manager,
            preprocessor,
            steps_manager,
        )


    @_run_once
    def init_multiscale_run(self):
        """TODO"""
        from multiscale_run import config, connection_manager, preprocessor
        from multiscale_run import utils as msr_utils
        self.config = config.MsrConfig(self._base_path)
        self.config.check()

        self.prep = preprocessor.MsrPreprocessor(self.config)

        self.managers = {}
        self.conn_m = connection_manager.MsrConnectionManager(
            config=self.config, managers=self.managers
        )
        # counter of neurodamus dts of the simulation. All simulation times
        # are based on this
        self.idts = 0
        self.prep.autogen_node_sets()
        self.rss = []  # Memory tracking

        self.time_steps = msr_utils.timesteps(self.config.run.tstop, self.config.multiscale_run_dt)

    @_run_once
    def init_neurodamus(self):
        """TODO"""

        from multiscale_run import (
            neurodamus_manager,
            reporter,
        )
        self.managers["neurodamus"] = neurodamus_manager.MsrNeurodamusManager(self.config)
        # this is here because neurodamus is in charge of setting the log level
        logging.info(str(self.config.multiscale_run))
        logging.info(self.config.dt_info())

        # this keeps track of the failed cells for all the simulators
        self.failed_cells = [None]*len(self.managers["neurodamus"].ncs)

        # create connection matrices
        self.conn_m.connect_neurodamus2neurodamus()

    @_run_once
    def init_metabolism(self):
        self.managers["metabolism"] = None
        if self.config.is_metabolism_active():
            from multiscale_run import (
                metabolism_manager,
            )
            self.managers["metabolism"] = metabolism_manager.MsrMetabolismManager(
                config=self.config,
                neuron_pop_name=self.managers["neurodamus"].neuron_manager.population_name,
                ncs=self.managers["neurodamus"].ncs,  # libsonata wants gids without offset
            )

    def sync(self):
        """Process syncs and cleanup (in case of recoverable failures)"""
        self.conn_m.sync(idts = self.idts)
        if self.config.is_metabolism_active():
            self.managers["metabolism"].check_inputs(failed_cells=self.failed_cells)
        self.conn_m.remove_gids(failed_cells=self.failed_cells)

    @_run_once
    def init(self):
        self.warmup()
        from neurodamus.utils.timeit import timeit
        logging.info("init simulation")

        with timeit(name="initialization"):
            self.init_multiscale_run()
            self.init_neurodamus()
            self.init_metabolism()

            self.sync()

    @_run_once
    def finalize(self):
        from neurodamus.utils.timeit import TimerManager
        """Final printing of files, after the loop"""
        self.managers["neurodamus"].ndamus.sonata_spikes()
        TimerManager.timeit_show_stats()
        utils.comm().Barrier()
        self.managers["neurodamus"].ndamus._touch_file(self.managers["neurodamus"].ndamus._success_file)

    @_run_once
    def compute(self):
        """Perform the actual simulation"""
        self.init()
        logging.info("Starting simulation")

        # Memory tracking
        import psutil
        from neurodamus.core import ProgressBarRank0 as ProgressBar
        from neurodamus.utils.timeit import timeit

        for t in ProgressBar(len(self.time_steps))(self.time_steps):
            self.idts += self.config.multiscale_run.ndts

            with timeit(name="main_loop"):
                self.managers["neurodamus"].solve(idts=self.idts)

                if self.config.is_metabolism_active():
                    self.managers["metabolism"].solve(idts=self.idts, failed_cells=self.failed_cells)

                self.sync()

                self.rss.append(
                    psutil.Process().memory_info().rss / (1024**2)
                )

        self.finalize()


def main():
    logging.basicConfig(level=logging.INFO)
    sim = MsrSimulation()
    sim.main()


if __name__ == "__main__":
    main()


