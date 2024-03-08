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
        liste = list(i for i in range(1,n+1))
        return list(permutations(liste))
    
    def grilles_comme_tuples(self):
        """
        Transforme une grille en tuple
        """
        TPL = []
        for k in range(len(self.state)): #nombre de lignes
            TPL.append(tuple(self.state[k])) #on rajoute chaque ligne de la grille sous forme de tuple
        TPL = tuple(TPL) #en fait un tuple de tuples
        return TPL

    #on part de ces listes et on les met sous forme de grilles. Renvoie tous les états possible de la grille 
    def liste_de_noeuds(self): 
        tous_les_noeuds = []
        liste = Grid.permut(self.m*self.m) #liste de toutes les permutations possibles
        for i in liste :
            noeud = []
            grille = list(i) 
            #on découpe la liste pour constituer les lignes
            for k in range(self.m): 
                noeud.append(grille[self.n*k:(k+1)*self.n])
            # on convertit tout en tuples pour que ce soit immuable 
            for k in range(len(noeud)):
                noeud[k] = tuple(noeud[k])
            noeud = tuple(noeud)
            tous_les_noeuds.append(noeud)
        return tous_les_noeuds # on crée une liste tous_les_noeuds qui contient des tuples qui représentent tous les états de la grille 

    def construire_le_graph(self): 
        tous_les_noeuds = self.liste_de_noeuds()
        graph_etats_grille = Graph(tous_les_noeuds)
    
        #tous_les_noeuds est un tuple que l'on convertit en liste 
        for etat in tous_les_noeuds : 
            liste_grille = [[] for k in range(len(etat))] #liste vide
            for ligne in range(len(etat)): 
                for colonne in range(len(etat[ligne])):
                    liste_grille[ligne].append(etat[ligne][colonne])
    
            #On a obtenu une liste de listes que l'on transforme en grille 
            grille = Grid(len(liste_grille),len(liste_grille[0]),liste_grille)

             #on crée les arrêtes entre deux grilles reliées par un swap horizontal
            for colonne in range(grille.n-1):
                for ligne in range(grille.m):
                    grille2 = copy.deepcopy(grille)
                    grille2.swap((ligne,colonne),(ligne, colonne +1))
                    graph_etats_grille.add_edge(grille.grilles_comme_tuples(),grille2.grilles_comme_tuples())
            
            #on fait de même pour deux grilles reliées par un swap vertical 
            for ligne in range(grille.m-1):
                for colonne in range(grille.n):
                    grille2 = copy.deepcopy(grille)
                    grille2.swap((ligne,colonne),(ligne+1,colonne))
                    graph_etats_grille.add_edge(grille.grilles_comme_tuples(),grille2.grilles_comme_tuples())

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

        Parameters: 
        -----------
        grid: Grid
            la grille d'origine

        Output: 
        -------
        liste_adj : list[tuple]
            une liste de tuples
        """

        liste_adj = []

        # On fait tous les swaps horizontaux et on ajoute les edges
        for i in range(self.n-1):
            for j in range(self.m):
                adj = self.copy()
                ajd.swap((j,i),(j,i+1))
                liste_adj.append((adj.grilles_comme_tuples(),((j,i),(j,i+1))))

        # On fait tous les swaps verticaux on ajoute les edges
        for i in range(self.m-1):
            for j in range(self.n):
                adj = self.copy()
                adj.swap((i,j),(i+1,j))
                liste_adj.append((other.grilles_comme_tuples(),((i,j),(i+1,j))))
        
        return liste_adj   
 

