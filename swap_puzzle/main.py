import os
from grid import Grid

g = Grid(2, 3)
print(g)

data_path = "../input/"
file_name = os.path.join('input', 'grid0.in')

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)