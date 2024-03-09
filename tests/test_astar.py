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
        solution = Grid(2,2).grilles_comme_tuples()  # Grille ordonnée
        
        # Appel de la méthode A* pour trouver le chemin
        chemin = A_star(g)

        # Appliquer les swaps selon le chemin obtenu pour vérifier si on aboutit à la solution
        grille_test = copy.deepcopy(g)
        for swap in chemin:
            grille_test.swap(*swap)
        
        print(grille_test)
        print(f"le chemin est le suivant: {chemin}")
        print(f"la longueur du chemin est: {len(chemin)}")

        # Vérification si la grille obtenue est égale à la solution
        assert grille_test.grilles_comme_tuples() == solution, "La méthode A* n'a pas trouvé la solution correcte."

if __name__ == '__main__':
    unittest.main()

""" ce test teste la méthode A* numéro 1 qui fonctionne avec la classe SolverRandom 
et qui ne peut donc pas traiter les grilles trop grandes
"""