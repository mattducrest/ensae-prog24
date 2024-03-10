import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import A_star2
import copy 

class Test_Astar2(unittest.TestCase): 
    def test_A_star2(self):
        # Grille de test
        g = Grid.grid_from_file("input/grid2.in") 
        
        # Appel de la méthode A* pour trouver le chemin
        chemin = A_star2(g)

        # Appliquer les swaps selon le chemin obtenu pour vérifier si on aboutit à la solution
        grille_test = copy.deepcopy(g)
        for swap in chemin:
            grille_test.swap(*swap)
        
        print(grille_test)
        print(f"le chemin est le suivant: {chemin}")
        print(f"la longueur du chemin est: {len(chemin)}")


if __name__ == '__main__':
    unittest.main()

""" 
quand on lance le test Astar2 on voir bien comment la grille est en train d'être triée mais 
contrairement à astar1 Astar2 ne renvoie pas le bon chemin ni le bon nombre de swaps

Pour que Astar2 renvoie le chemin et le nombre de swaps il faudrait que get solution soit la suivante : 
@staticmethod
def get_ solution (grid):
    sequence_swaps= []
    for x in range(1, grid.m * grid.n + 1) :
        SolverSearch.drag_x(grid, x, sequence_swaps)
    return sequence_swaps

""" 