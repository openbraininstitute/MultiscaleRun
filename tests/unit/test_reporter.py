from pathlib import Path

import h5py
import numpy as np

from multiscale_run import MsrConfig, MsrReporter, utils


def config_path():
    return Path(__file__).resolve().parent / "test_folder" / "simulation_config.json"


class FakeNeurodamusManager:
    def __init__(self) -> None:
        self.name = "neurodamus"
        self.circuit_offset = 1000
        gids = {0: [0, 1], 1: [6], 2: [], 3: [5, 7, 11]}
        ps = np.cumsum([len(i) for i in gids.values()])
        ps = [0, *ps[:-1]]
        self.offset = ps[utils.rank()]
        self._gids = gids[utils.rank()]
        self.base_gids = gids.copy()

    def gids(self, raw=False):
        if raw:
            return self._gids
        else:
            return [i + self.circuit_offset for i in self._gids]


class FakeMetabolismManager:
    def __init__(self, raw_gids) -> None:
        self.name = "metabolism"
        vals = {
            0: [0] * len(raw_gids),
            1: [1] * len(raw_gids),
            2: [2] * len(raw_gids),
            3: [3] * len(raw_gids),
        }
        self.vals = np.array([[-1 for _ in raw_gids], vals[utils.rank()]]).transpose()

    def get_vals(self, idx = 0):
        return self.vals[:, idx]


def test_simple_reports():
    conf = MsrConfig(config_path())
    folder_path = conf.config_path.parent / conf.output.output_dir

    utils.remove_path(folder_path)

    pop_name = conf.multiscale_run.preprocessor.node_sets.neuron_population_name
    idt = 1
    managers = {}
    managers["neurodamus"] = FakeNeurodamusManager()
    gids = managers["neurodamus"].gids(raw=True)
    offset = managers["neurodamus"].offset
    managers["metabolism"] = FakeMetabolismManager(raw_gids=managers["neurodamus"].gids(raw=True))

    t_unit = "mss"

    rr = MsrReporter(config=conf, gids=gids, t_unit=t_unit)

    rr.init_files(simulator="metabolism", dt=conf.metabolism_dt, is_post_adv=False)
    rr.init_files(simulator="metabolism", dt=conf.metabolism_dt, is_post_adv=True)

    rr.record(idt=idt, simulator=managers["metabolism"], gids=gids, is_post_adv=False)
    rr.record(idt=idt, simulator=managers["metabolism"], gids=gids, is_post_adv=True)
    utils.comm().Barrier()

    for title, rep in conf.multiscale_run.metabolism.reports.items():
        for is_post_adv in [False, True]:
            path = rr._file_path(title, rep, is_post_adv=is_post_adv)
            if not path:
                continue
            with h5py.File(path, "r") as file:
                data = file[f"{rr._data_loc}/data"]
                assert np.allclose(
                    data[idt, offset : offset + len(gids)],
                    managers["metabolism"].get_vals(**rep.get("src_get_kwargs", {})),
                )
                assert np.allclose(data[idt - 1, offset : offset + len(gids)], [0] * len(gids))
                assert data.attrs["units"] == rep.get("unit", '')
                data = file[f"/report/{pop_name}/mapping/node_ids"]
                assert np.allclose(data[offset : offset + len(gids)], [i for i in gids])
                data = file[f"/report/{pop_name}/mapping/time"]
                time_array = [conf.metabolism_dt, conf.run.tstop+conf.metabolism_dt, conf.metabolism_dt] if is_post_adv else [0, conf.run.tstop, conf.metabolism_dt] 
                assert np.allclose(data, time_array)
                assert data.attrs["units"] == t_unit

    utils.remove_path(folder_path)


if __name__ == "__main__":
    test_simple_reports()
