import sys 
import time
sys.path.append("swap_puzzle/")

from grid import Grid
from solver import SolverRandom
import unittest

class Test_Solver(unittest.TestCase):
    def test_grid2(self):
        g1 = Grid.grid_from_file("input/grid2.in")
        print(g1)
        start_time = time.time()
        SolverRandom.get_solution(g1)
        print(g1)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"The function took {elapsed_time} seconds to run.")

    
"""""
    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        print(g)
        print(Grid.is_sorted(g))
        SolverRandom.get_solution(g)
        print(Grid.is_sorted(g))

"""""

if __name__ == '__main__':
    unittest.main()