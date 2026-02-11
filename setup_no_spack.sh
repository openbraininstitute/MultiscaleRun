#!/usr/bin/env bash

test_folder="tiny_CI_test"

if [[ "$(uname -s)" == "Darwin" ]]; then
    PLATFORM=mac
elif [[ -f /sys/class/dmi/id/sys_vendor ]] && grep -qi 'microsoft' /sys/class/dmi/id/sys_vendor; then
    PLATFORM=azure
elif [[ -f /etc/os-release ]] && grep -qi '^name="Amazon Linux"' /etc/os-release; then
    PLATFORM=aws
else
    PLATFORM=unknown
    echo "WARNING: Unable to detect platform (mac / aws / azure)" >&2
    return 1
fi

echo "Detected platform: $PLATFORM"

# ------------------------------------------------------------------------------
# Common environment
# ------------------------------------------------------------------------------
export LIBSONATA_ZERO_BASED_GIDS=1
export OMP_NUM_THREADS=1

export SONATAREPORT_DIR="$(pwd)/libsonatareport/build/install"
export NEURODAMUS_NEOCORTEX_ROOT="$(pwd)/neurodamus-models/build/install"
export HOC_LIBRARY_PATH="$NEURODAMUS_NEOCORTEX_ROOT/share/neurodamus_neocortex/hoc"

export HDF5_MPI=ON

# ------------------------------------------------------------------------------
# OS-specific configuration
# ------------------------------------------------------------------------------

if [[ "$PLATFORM" == "mac" ]]; then
  export PATH="/opt/homebrew/bin:$PATH"
  export LDFLAGS="-L/opt/homebrew/opt/openmpi/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/openmpi/include"

  export HDF5_INCLUDEDIR=$(brew --prefix hdf5-mpi)/include
  export HDF5_LIBDIR=$(brew --prefix hdf5-mpi)/lib

  export CORENEURONLIB="$NEURODAMUS_NEOCORTEX_ROOT/lib/libcorenrnmech.dylib"
  export NRNMECH_LIB_PATH="$NEURODAMUS_NEOCORTEX_ROOT/lib/libnrnmech.dylib"
elif  [[ "$PLATFORM" == "azure" ]]; then
  export HDF5_INCLUDEDIR=/usr/include/hdf5/mpich
  export HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/mpich

  export CORENEURONLIB="$NEURODAMUS_NEOCORTEX_ROOT/lib/libcorenrnmech.so"
  export NRNMECH_LIB_PATH="$NEURODAMUS_NEOCORTEX_ROOT/lib/libnrnmech.so"
else
  export PATH=/opt/amazon/openmpi5/bin:$PATH
  export LD_LIBRARY_PATH=/opt/amazon/openmpi5/lib64:$LD_LIBRARY_PATH

  export PATH=/opt/circuit_simulation/hdf5/hdf5-1.14.6/install/bin:$PATH
  export LD_LIBRARY_PATH=/opt/circuit_simulation/hdf5/hdf5-1.14.6/install/lib:$LD_LIBRARY_PATH

  export HDF5_INCLUDEDIR=/opt/circuit_simulation/hdf5/hdf5-1.14.6/install/include
  export HDF5_LIBDIR=/opt/circuit_simulation/hdf5/hdf5-1.14.6/install/lib

  export CORENEURONLIB="$NEURODAMUS_NEOCORTEX_ROOT/lib/libcorenrnmech.so"
  export NRNMECH_LIB_PATH="$NEURODAMUS_NEOCORTEX_ROOT/lib/libnrnmech.so"
fi

export CC=$(which mpicc)
export CXX=$(which mpicxx)
export MPICC=$(which mpicc)

if [[ -n "$VIRTUAL_ENV" ]]; then
    deactivate
fi

if [ -d "venv" ]; then
  echo "Found existing venv directory. Just load env"
  source venv/bin/activate
else
  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade pip setuptools
  pip install NEURON-nightly cython
  pip cache purge
  pip install --no-binary=mpi4py mpi4py
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

