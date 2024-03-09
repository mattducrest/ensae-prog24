import sys 
import time
sys.path.append("swap_puzzle/")

from grid import Grid
from solver import SolverSearch
import unittest

class Test_Solver(unittest.TestCase):
    def test_grid2(self):
        g1 = Grid.grid_from_file("input/grid2.in")
        print(g1)
        m, n = g1.m, g1.n
        initial_state = g1.state
        solver = SolverSearch(m, n, initial_state)
        start_time = time.time()
        solution = solver.get_solution()
        print(solver.grid)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"The function took {elapsed_time} seconds to run.")


if __name__ == '__main__':
    unittest.main()
