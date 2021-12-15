from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import numpy as np


def gm(ma):
    ma = (ma + 1) % 10
    ma = np.where(ma == 0, 1, ma)
    return ma


with open("data.txt", "r") as file:
    data = file.readlines()
m = np.array([[int(i) for i in x[:-1]] for x in data])
tile = np.concatenate([m, gm(m), gm(gm(m)), gm(gm(gm(m))), gm(gm(gm(gm(m))))], 1)
tile = np.concatenate([tile, gm(tile), gm(gm(tile)), gm(gm(gm(tile))), gm(gm(gm(gm(tile))))], 0)
matrix = m  # or for part 2 matrix = tile
grid = Grid(matrix=matrix)
start = grid.node(0, 0)
end = grid.node(len(matrix[-1]) - 1, len(matrix) - 1)

finder = AStarFinder()
path, _ = finder.find_path(start, end, grid)
risk = 0
for i, j in path[1:]:
    risk += matrix[j][i]
print(risk)
