import time
import numpy as np
from day1.with_numpy import calc_sliding as func

runs = 100

with open("day1/data.txt", "r") as file:
    depth = file.read().splitlines()
depth = [int(i) for i in depth]

# depth = np.loadtxt("day1/data.txt", dtype=int, delimiter="\n", )

start = time.time()
for i in range(runs):
    func(depth)
print((time.time() - start) / runs)
