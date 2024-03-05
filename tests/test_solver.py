import sys 
sys.path.append("swap_puzzle/")

from grid import Grid
from solver import SolverRandom
import unittest

"""""
g = Grid.grid_from_file("input/grid1.in")

print(g)
print(Grid.is_sorted(g))

Solver.get_solution(g)
print(Grid.is_sorted(g))

"""""

class Test_Solver(unittest.TestCase):
    def test_grid2(self):
        g1 = Grid.grid_from_file("input/grid2.in")
        print(g1)
        SolverRandom.get_solution(g1)
        print(g1)

if __name__ == '__main__':
    unittest.main()