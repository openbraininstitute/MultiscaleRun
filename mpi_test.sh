#!/usr/bin/env bash
set -e

# Use the venv python explicitly
PYTHON_BIN="${VIRTUAL_ENV:-./venv}/bin/python"

# Debug info
echo "mpirun: $(which mpirun)"
echo "mpicc: $(which mpicc)"
echo "python: $PYTHON_BIN"

# Run simple 2-rank MPI test
/usr/bin/mpirun -n 2 $PYTHON_BIN - << 'EOF'
from mpi4py import MPI
comm = MPI.COMM_WORLD
print("rank", comm.Get_rank(), "size", comm.Get_size())
total = comm.allreduce(1, op=MPI.SUM)
assert total == 2
print("MPI test passed!")
EOF