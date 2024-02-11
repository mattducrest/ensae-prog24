"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random

from math import *

class Grid():
    """"
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intial state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        L =[]
        "Verification des diagonales ok"
        for k in range(self.m-1):
            if (self.state[k][self.n-1] == self.state[k+1][0]-1):
                L.append(True)
            else:
                L.append(False)
        
        "Verification de l'incrémentation ligne par ligne"
        for k in range(self.m):
            for i in range (self.n-1):
                if (self.state[k][i] == self.state[k][i+1]-1):
                    L.append(True)
                else:
                    L.append(False)

        "Verification de tout"
        for i in range(len(L)):
            if L[i] is not True:
                return False
        
        return True

        
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
  

    def swap(self, cell1, cell2):
        i1, j1 = cell1
        i2, j2 = cell2

        if (abs(i1-i2) == 1 and j1 == j2) or (abs(j1-j2) == 1 and i1 == i2) : 
            S = self.state[i1][j1] 
            self.state[i1][j1]  = self.state[i2][j2]
            self.state[i2][j2] = S 
        
        else :
            return None

        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
    

    def swap_seq(self, cell_pair_list):
        for k in range(len(cell_pair_list)): 
            c1, c2 = cell_pair_list[k]
            self.swap(c1, c2)

        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid

    # Question 6 : on réfléchit à une représentation des noeuds qui correspond à tous les états de la grille

      def __hash__(self):
        return hash(tuple(map(tuple, self.state)))
    # Il faut que les noeds soient de type hashable. Grace à map() on applique la fonction tuple à tous les éléments de la grille
    # Ainsi chaque ligne de la grille devient un tuple 
    # Enfin on fait un tuple unique de tous nos tuples 
    # hash s'assure que le tuple ets bien hashable 



    def __eq__(self, other):
        return isinstance(other, Grid) and self.state == other.state
    
    # Cette méthode permet de comparer si deux noeuds sont égaux ou non 
    # On vérifie d'abord que les deux noeuds sont bien des objets de grid 
    # Puis on les compare 

    # Le problème de cette fonction est qu'elle construit le graph mais ne considérent qu'un swap. Elle n'effectue pas de swaps consécutuifs donc on n'a pas tous les états de la grille 
    def build_graph(self):
        graph = {}
        # Parcourir tous les états possibles de la grille
        for i in range(self.m): # i représente les lignes
            for j in range(self.n): # j représente les colonnes 
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # on peut aller dans 4 directions : droite bas gauche haut 
                    ni, nj = i + di, j + dj
                    while 0 <= ni < self.m and 0 <= nj < self.n: # on vérifie que l'on est pas au bord de la grille 
                        # Effectuer un coup de swap entre les nombres à la position (i, j) et (ni, nj)
                        new_state = self.swap(i, j, ni, nj)
                        if self.state not in graph: # on ne veut pas avoir deux fois le même état de la grille 
                            graph[self] = [] # on ajoute une nouvelle entrée au dictionnaire graph, sa valeur est vide pour stocker d'éventuels voisins 
                        if new_state not in graph:
                            graph[new_state] = []
                        # Ajouter une arête entre l'état actuel et le nouvel état dans le graphe
                        graph[self].append(new_state) #On ajoute le nouvel état comme voisin d el'actuel état dans le graph 
                        graph[new_state].append(self)
        return graph

     # Méthode qui trouve une solution de longueur optimale pour le swap puzzle 



    