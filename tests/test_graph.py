import sys 
sys.path.append("swap_puzzle/")

import unittest 

from grid import Grid

class Test_graph(unittest.TestCase):
    def test_graph1(self): 
        g = Grid.grid_from_file("input/grid_test_graph")
        resultat_observe = grid.construire_le_graph(g) 

        resultat_attendu = {}
        resultat_attendu[tuple(map(tuple, g.state))] = [row[:] for row in g.state]
        noeud_initial = graph[g.state]
        new_state = g.swap((0,0), (0,1))
        resultat_attendu[tuple(map(tuple, new_state.state))] = [row[:] for row in new_state.state]
        resultat_attendu[noeud_initial].append(new_state) 
        resultat_attendu[new_state].append(noeud_initial) 

        self.assertEqual(resultat_attendu, resultat_observe)

if __name__ == '__main__':
    unittest.main()