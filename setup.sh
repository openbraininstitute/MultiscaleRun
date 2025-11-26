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





