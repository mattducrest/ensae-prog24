"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
import copy
from graph import Graph 
import matplotlib.pyplot as plt
from itertools import permutations 
import numpy as np 

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
        Checks is the current state of the grid is sorted and returns the answer as a boolean.
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


    def __representation__(self) : 
    # Représentation graphique de la grille 
    # la matrice que l'on veut afficher 
         matrice = self.state 

         plt.imshow(matrice, cmap='viridis', interpolation='nearest')
         plt.colorbar(label='Values')
         plt.title('représentation graphique de la grille sous forme d une matrice')
         plt.show()

    # Question 6 : on réfléchit à une représentation des noeuds qui correspond à tous les états de la grille

    #on trouve les listes qui correspondent à toutes les permutations de la grille 
    @classmethod
    def permut(cls, n):
        return list(permutations(range(1, n + 1)))

    def grilles_comme_tuples(self):
        TPL = []
        for k in range(len(self.state)):
            TPL.append(tuple(self.state[k]))
        return tuple(TPL)

    def liste_de_noeuds(self):
        tous_les_noeuds = []
        self.state_to_id = {}
        self.id_to_state = {}
        liste = Grid.permut(self.m * self.n)
        for i, perm in enumerate(liste):
            noeud = [perm[j * self.n:(j + 1) * self.n] for j in range(self.m)]
            noeud_tuple = tuple(tuple(row) for row in noeud)
            if noeud_tuple not in self.state_to_id:
                node_id = len(self.state_to_id) + 1
                self.state_to_id[noeud_tuple] = node_id
                self.id_to_state[node_id] = noeud_tuple
                tous_les_noeuds.append(node_id)
        return tous_les_noeuds

    def construire_le_graph(self):
        from graph import Graph  # Make sure to have the Graph class defined or imported correctly

        tous_les_noeuds = self.liste_de_noeuds()
        graph_etats_grille = Graph(tous_les_noeuds)

        for etat_id in tous_les_noeuds:
            etat = self.id_to_state[etat_id]
            grille = Grid(self.m, self.n, [list(row) for row in etat])
            for ligne in range(grille.m):
                for colonne in range(grille.n):
                    if colonne < grille.n - 1:  # Swap right
                        grille2 = copy.deepcopy(grille)
                        grille2.swap((ligne, colonne), (ligne, colonne + 1))
                        graph_etats_grille.add_edge(etat_id, self.state_to_id[grille2.grilles_comme_tuples()])
                    if ligne < grille.m - 1:  # Swap down
                        grille3 = copy.deepcopy(grille)
                        grille3.swap((ligne, colonne), (ligne + 1, colonne))
                        graph_etats_grille.add_edge(etat_id, self.state_to_id[grille3.grilles_comme_tuples()])

        return graph_etats_grille

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

    def grilles_adjacentes(self):
        
        """
        Génère toutes les grilles atteignables en un swap à partir d'une grille donnée

        paramètres: 
        -----------
        grid: Grid
            la grille d'origine

        image: 
        -------
        liste_adj : list[tuple]
            une liste de tuples
        """

        liste_adj = []

        # On fait tous les swaps horizontaux et on ajoute les edges
        for i in range(self.n-1):
            for j in range(self.m):
                adj = copy.deepcopy(self)
                adj.swap((j,i),(j,i+1))
                liste_adj.append((adj.grilles_comme_tuples(),((j,i),(j,i+1))))

        # On fait tous les swaps verticaux on ajoute les edges
        for i in range(self.m-1):
            for j in range(self.n):
                adj = copy.deepcopy(self)
                adj.swap((i,j),(i+1,j))
                liste_adj.append((adj.grilles_comme_tuples(),((i,j),(i+1,j))))
        
        return liste_adj   
 

