import sys 
sys.path.append("swap_puzzle/")

from grid import Grid
from solver import Solver

"""""
g = Grid.grid_from_file("input/grid1.in")

print(g)
print(Grid.is_sorted(g))

Solver.get_solution(g)
print(Grid.is_sorted(g))

"""""
g1 = Grid.grid_from_file("input/grid2.in")

Solver.get_solution(g1)


