# !/usr/bin/env bash

test_folder="tiny_CI_test"

# libsoantareport

export LIBSONATA_ZERO_BASED_GIDS=1

# spack

if [ -d "spackenv" ]; then
  echo "Found existing spackenv directory. Just load env"
  spack env activate -d spackenv
else
  spack env create -d spackenv
  spack env activate -d spackenv
  spack add neurodamus-models@develop+ngv+metabolism model=neocortex
  spack add py-neurodamus@develop
  spack add openmpi
  spack concretize -f
  spack install
  spack env deactivate
  spack env activate -d spackenv
fi

# julia

JULIAENV_DIR="$PWD/juliaenv"
export PYTHON=$(which python3)
export JULIA_NUM_THREADS=1
export JULIA_DEPOT_PATH="$PWD/$JULIAENV_DIR"
export JULIAUP_DEPOT_PATH="$JULIA_DEPOT_PATH"
export JULIA_PROJECT="$PWD/juliaenv"

# Skip setup if the environment already exists
if [ -d "$JULIAENV_DIR" ]; then
  echo "✓ Julia environment already exists at '$JULIAENV_DIR'. Skipping setup."
else
  mkdir -p "$JULIAENV_DIR"
  
  julia --color=yes -e "
using Pkg

# Activate environment
Pkg.activate(\"$JULIAENV_DIR\")

println(\"→ Installing Julia packages...\")

# Add required packages
for pkg in [\"IJulia\", \"PyCall\", \"PythonCall\", \"DifferentialEquations\"]
    Pkg.add(pkg)
end

# Ensure environment is synced
Pkg.instantiate(verbose=true)

# Precompile all packages
Pkg.precompile()

println(\"✓ Julia packages installation complete.\")
"
fi


# python

if [ -d "venv" ]; then
  echo "Found existing venv directory. Just load env"
  source venv/bin/activate
else
  python -m venv venv
  source venv/bin/activate
  pip install --upgrade pip
  pip install -e .
fi

# set new test

if [ ! -d "$test_folder" ]; then
  multiscale-run init "$test_folder" --circuit=tiny_CI
  cd $test_folder
  source ../.ci/setup.sh
  download_tiny_CI_neurodamus_data
  cd ..
fi

# # manually edit set simplation_config.json

# # run

# # multiscale-run compute





