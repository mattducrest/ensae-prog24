import sys 
sys.path.append("swap_puzzle/")
from grid import Grid

grid = Grid(3, 3)
grid_state = [[2, 1, 3], [4, 5, 6], [7, 8, 9]]

# Call liste_de_noeuds to initialize the state_to_id dictionary
grid.liste_de_noeuds()

# Convert the grid state to a tuple of tuples
state_tuple = tuple(tuple(row) for row in grid_state)

# Check if the state_tuple is in the state_to_id dictionary
if state_tuple in grid.state_to_id:
    node_id = grid.state_to_id[state_tuple]
    print(f"The node ID for the given state is: {node_id}")
else:
    print("Invalid grid state.")

"""""   
node_id = grid.get_node_id_from_state(grid_state)
print(f"The node ID for the given state is: {node_id}")
"""