import sys 
sys.path.append("swap_puzzle/")

from grid import Grid

g= Grid.grid_from_file("input/grid2.in")

print(construire_le_graph(g)) 

