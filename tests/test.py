import sys 
sys.path.append("swap_puzzle/")

from graph import Graph

graph = Graph.graph_from_file("input/graph1.in")
print(graph)