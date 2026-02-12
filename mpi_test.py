from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print(f"Rank {rank} of {size}")
total = comm.allreduce(1, op=MPI.SUM)
assert total == 2
print("MPI test passed!")