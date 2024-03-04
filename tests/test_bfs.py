
import sys 
sys.path.append("swap_puzzle/")


import unittest
from graph import Graph


class Test_BFS(unittest.TestCase):
    def test_graph1(self):
        graph = Graph.graph_from_file("input/graph1.in")
        resultat_observe = Graph.bfs(graph)
        with open("input/graph1.path.out", "r") as file:
            resultat_attendu = file.read()
        
        self.assertEqual(resultat_observe, resultat_attendu)
if __name__ == '__main__':
    unittest.main()


g = Graph.graph_from_file("input/graph1.in")
Graph.bfs(g)



