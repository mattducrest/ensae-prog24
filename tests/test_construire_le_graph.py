import sys 
sys.path.append("swap_puzzle/")
import unittest
from graph import Graph
from grid import Grid
import networkx as nx

class Test_graph(unittest.TestCase):

    def test_construire(self):
        g= Grid.grid_from_file("input/grid2.in")
        test = g.construire_le_graph()
        self.assertIsInstance(test, nx.Graph) 
    
if __name__ == '__main__':
    unittest.main()



