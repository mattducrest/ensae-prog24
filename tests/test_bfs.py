import sys 
sys.path.append("swap_puzzle/")

from graph import Graph

g = Graph.graph_from_file("input/graph1.in")

Graph.bfs(g)
