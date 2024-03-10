import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import A_star
import copy 

class Test_Astar(unittest.TestCase): 
    def test_A_star(self):
        # Grille de test
        g = Grid.grid_from_file("input/grid0.in") 
        
        # Appel de la méthode A* pour trouver le chemin
        chemin = A_star(g)

        # Appliquer les swaps selon le chemin obtenu pour vérifier si on aboutit à la solution
        grille_test = copy.deepcopy(g)
        for swap in chemin:
            grille_test.swap(*swap)
        
        print(grille_test)
        print(f"le chemin est le suivant: {chemin}")
        print(f"la longueur du chemin est: {len(chemin)}")

        

if __name__ == '__main__':
    unittest.main()

""" ce test teste la méthode A* numéro 1 qui fonctionne avec la classe SolverRandom 
et qui ne peut donc pas traiter les grilles trop grandes
"""