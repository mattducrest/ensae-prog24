import sys 
sys.path.append("swap_puzzle/")
import unittest
from graph import Graph
from grid import Grid

#attention, c'est normal que bfs return none, il faut regarder le fichier output.txt pour voir les résultats

g = Grid.grid_from_file("input/grid0.in")
test = Grid.construire_le_graph(g)
bfs = Graph.get_solution_bfs_2(test)
print(bfs)


