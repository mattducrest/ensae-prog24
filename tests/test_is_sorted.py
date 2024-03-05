# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_IsSorted(unittest.TestCase):
    def test_grid1(self):
        grid = Grid.grid_from_file("input/grid1.in")
        self.assertEqual(grid.is_sorted(), False) #pour l'instant grid1 n'est pas ordonnée
        grid.swap((3,0), (3,1)) #on fait le swap nécessaire 
        self.assertEqual(grid.is_sorted(), True) #grid1 est ordonnée 

if __name__ == '__main__':
    unittest.main()