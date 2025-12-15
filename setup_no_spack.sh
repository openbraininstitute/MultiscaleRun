# !/usr/bin/env bash

test_folder="tiny_CI_test"

export PATH="/opt/homebrew/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/openmpi/lib"
export CPPFLAGS="-I/opt/homebrew/opt/openmpi/include"
# alias python=python3.11

export LIBSONATA_ZERO_BASED_GIDS=1
export OMP_NUM_THREADS=1
export SONATAREPORT_DIR=$(pwd)/libsonatareport/build/install
export NEURODAMUS_NEOCORTEX_ROOT=$(pwd)/neurodamus-models/build/install
export HOC_LIBRARY_PATH=$NEURODAMUS_NEOCORTEX_ROOT/share/neurodamus_neocortex/hoc
export CORENEURONLIB=$NEURODAMUS_NEOCORTEX_ROOT/lib/libcorenrnmech.dylib
export NRNMECH_LIB_PATH=$NEURODAMUS_NEOCORTEX_ROOT/lib/libnrnmech.dylib

export HDF5_INCLUDEDIR=$(brew --prefix hdf5-mpi)/include
export HDF5_LIBDIR=$(brew --prefix hdf5-mpi)/lib
export CC=$(which mpicc)
export CXX=$(which mpicxx)
export HDF5_MPI="ON" 
export HDF5_INCLUDEDIR=$HDF5_INCLUDEDIR 
export HDF5_LIBDIR=$HDF5_LIBDIR
export MPICC=$(brew --prefix openmpi)/bin/mpicc

deactivate

if [ -d "venv" ]; then
  echo "Found existing venv directory. Just load env"
  source venv/bin/activate
else
  python3.11 -m venv venv
  source venv/bin/activate
  pip install --upgrade pip
  pip install NEURON-nightly cython
  pip cache purge
  pip install --no-binary=mpi4py mpi4py
  python -m pip install --upgrade pip setuptools
  pip install --no-cache-dir --no-binary=h5py h5py --no-build-isolation
  pip install neurodamus morphio ruff pytest
fi

if [ ! -d "libsonatareport" ]; then
    git clone https://github.com/openbraininstitute/libsonatareport.git --recursive --depth=1
    cmake -B libsonatareport/build -S libsonatareport \
    -DCMAKE_INSTALL_PREFIX=$SONATAREPORT_DIR -DCMAKE_BUILD_TYPE=Release -DSONATA_REPORT_ENABLE_SUBMODULES=ON -DSONATA_REPORT_ENABLE_MPI=ON -GNinja

    cmake --build libsonatareport/build
    cmake --install libsonatareport/build
fi

if [ ! -d "neurodamus-models" ]; then
  git clone https://github.com/openbraininstitute/neurodamus-models.git

  DATADIR=$(python -c "import neurodamus; from pathlib import Path; print(Path(neurodamus.__file__).parent / 'data')")

  cmake -B neurodamus-models/build -S neurodamus-models/ \
      -DPython_EXECUTABLE=$(which python) \
      -DCMAKE_INSTALL_PREFIX=$NEURODAMUS_NEOCORTEX_ROOT \
      -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=ON \
      -DNEURODAMUS_CORE_DIR=${DATADIR} \
      -DCMAKE_PREFIX_PATH=$SONATAREPORT_DIR \
      -DNEURODAMUS_MECHANISMS=neocortex \
      -DNEURODAMUS_ENABLE_CORENEURON=OFF \
      -DNEURODAMUS_NCX_V5=ON \
      -DNEURODAMUS_NCX_METABOLISM=ON \
      -DNEURODAMUS_NCX_NGV=ON \
      -GNinja

  cmake --build neurodamus-models/build
  cmake --install neurodamus-models/build
fi

pip install -e .

if [ ! -d "$test_folder" ]; then
  multiscale-run init "$test_folder" --circuit=tiny_CI
  cd $test_folder
  source ../.ci/setup.sh
  download_tiny_CI_neurodamus_data
  cd ..
fi