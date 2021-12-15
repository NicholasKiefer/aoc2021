from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import numpy as np

with open("data.txt", "r") as file:
    data = file.readlines()
matrix = np.array([[int(i) for i in x[:-1]] for x in data])
grid = Grid(matrix=matrix)
start = grid.node(0, 0)
end = grid.node(len(matrix[-1]) - 1, len(matrix) - 1)

finder = AStarFinder()
path, _ = finder.find_path(start, end, grid)
risk = 0
for i, j in path[1:]:
    risk += matrix[j][i]
print(risk)
