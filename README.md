
## MultiscaleRun

MultiscaleRun is an orchestrator of simulators. Currently, only Neurodamus (NEURON) and Metabolism are used together in a dual run, with more integrations planned for the future. It uses the NEURON simulator for neuronal activity, coupled with a metabolism solver.

## Testing for Development

### Prerequisites

- have an OBI spack installation working: https://github.com/openbraininstitute/spack

### Setup

You just need to run the setup script at least once before running the simulation.

**With Spack** (requires OBI spack installation):
```bash
source setup.sh
```

The script does:

- set various env variables
- create a `spackenv` folder with the necessary dependencies
- create a python virtual env in `venv` 
- call `pip install -e .` for development
- create the test folder `tiny_CI_test`
- fill it with the necessary data

If a folder is present (`spackenv`, `venv`) the script skips that installation step assuming that is already done. If any of the folders are missing, the script redoes the setup. 

The environment is still set as it is needed. 

You can always modify them and recall the setup script. It will not override your changes. 

**Without Spack** (uses Homebrew on macOS):

In this case we leverage brew. First we need to install a few things:

```bash
brew install cmake openmpi hdf5-mpi python@3.11 ninja
```

Finally, you need to run this at least once before running simulations:

```bash
source setup_no_spack.sh
```

The script does:

- set various env variables
- create a python virtual env in `venv` with neuron and neurodamus
- build `libsonatareport`
- build the correct `neurodamus-models`
- call `pip install -e .` for development
- create the test folder `tiny_CI_test`
- fill it with the necessary data


If a folder is present (`libsonatareport`, `neurodamus-models`, `venv`) the script skips that installation step assuming that is already done. If any of the folders are missing, the script redoes the setup. 

The environment is still set as it is needed. 

You can always modify them and recall the setup script. It will not override your changes. 

### Test

You just need to go to `tiny_CI_test` and run. The simulation is too slow with just one core. I suggest at least 8 cores. Do not go above 90 for now as this leaves some cores without neurons (edge case that I did not check). 

```bash
cd tiny_CI_test
mpirun -np 12 multiscale-run compute
```

#### Note

At the moment this simulation depleates atpi and fails after 300 ms. TODO: fix it.

#### Postprocessing

After the simulation has completed you can check the results with the postproc jupyter notebook. It is already in the current folder. Just run jupyter:

```bash
jupyter lab
```

open `postproc.ipynb` and run. By default it presents all the traces for the gids `[0, 1, 2]`. The notebook should be self-explainatory and can be changed at will. 

#### Unit tests

Locally, we use tox to run the unit tests:

```bash
pip install tox
tox -e unit
```

### Docs

Build the documentation locally with:

```bash
tox -e docs
```

Alternatively, check the official documentation at: https://multiscalerun.readthedocs.io/stable/

## Authors

Polina Shichkova, Alessandro Cattabiani, Christos Kotsalos, and Tristan Carel

## Acknowledgment

The development of this software was supported by funding to the Blue Brain Project,
a research center of the École polytechnique fédérale de Lausanne (EPFL),
from the Swiss government's ETH Board of the Swiss Federal Institutes of Technology.

Copyright (c) 2005-2023 Blue Brain Project/EPFL
Copyright (c) 2025 Open Brain Institute