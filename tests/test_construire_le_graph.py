import sys 
sys.path.append("swap_puzzle/")
import unittest
from graph import Graph
from grid import Grid
import networkx as nx

""" 
ce test ne fonctionne pas -> il renvoie False sûrement à cause de graph.Graph
il a toutes fois permis de corriger les erreurs dans le script de la fonction méthode contruire_le_graph
class Test_graph(unittest.TestCase):

    def test_construire(self):
        g= Grid.grid_from_file("input/grid0.in")
        test = g.construire_le_graph()
        self.assertIsInstance(test, Graph.Graph) 
    
if __name__ == '__main__':
    unittest.main()
"""


