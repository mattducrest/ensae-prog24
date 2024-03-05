

import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_Visualisation(unittest.TestCase):
    def test_imshow(self): 
        g = Grid.grid_from_file("input/grid1.in")
        print(g.__representation__()) 
    
if __name__ == '__main__':
    unittest.main()