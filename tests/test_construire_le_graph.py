import sys 
sys.path.append("swap_puzzle/")
import unittest
from graph import Graph
from grid import Grid

class Test_graph(unittest.TestCase):

    def construire(self):
        g= Grid.grid_from_file("input/grid2.in")
        Graph = g.construire_le_graph()
        print(Graph)
        return Graph
    
if __name__ == '__main__':
    unittest.main()



