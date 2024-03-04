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
    

    def __repgraph__(self) : 
    # Représentation graphique de la grille 
    
         import matplotlib.pyplot as plt 
         import numpy as np 

    # la matrice que l'on veut afficher 
         matrice = self.state 

         plt.imshow(matrice, cmap='viridis', interpolation='nearest')
         plt.colorbar(label='Values')
         plt.title('représentation graphique de la grille sous forme d une matrice')
         plt.show()

    # Question 6 : on réfléchit à une représentation des noeuds qui correspond à tous les états de la grille

    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))
    # Il faut que les noeuds soient de type hashable. Grace à map() on applique la fonction tuple à tous les éléments de la grille
    # Ainsi chaque ligne de la grille devient un tuple 
    # Enfin on fait un tuple unique de tous nos tuples 
    # hash s'assure que le tuple ets bien hashable 



    def __eq__(self, other):
        return isinstance(other, Grid) and self.state == other.state
    
    # Cette méthode permet de comparer si deux noeuds sont égaux ou non 
    # On vérifie d'abord que les deux noeuds sont bien des objets de grid 
    # Puis on les compare 


######

    #on trouve les listes qui correspondent à toutes les permutations de la grille 
    def permutation(cls, n):
        liste = list(i, for i in range(1,n+1))
        return list(permutations(list))

    #on part de ces listes et on les met sous forme de grilles 
    def liste_de_noeuds(self): 
        noeud = []
        liste = Grid.permu(self.n*self.m) #liste de toutes les permutations possibles
        for i in liste :
            noeud = []
            grille = list(i) 
            #on découpe la liste pour constituer les lignes
            for k in range(self.m): 
                node.append(grille[self.n*k:(k+1)*self.n])
            # on convertit tout en tuples pour que ce soit immuable 
            for k in range(len(noeud)):
                noeud[k] = tuple(noeud[k])
            noeud = tuple(noeud)
            noeud.append(noeud)
        return noeud # on crée une liste noeud qui contient des tuples qui représentent tous les états de la grille 

    def construire_le_graph(self): 
        noeud = self.liste_de_noeuds()
        graph_etats_grille = Graph(noeud)
    
        #noeud est un tuple que l'on convertit en liste 
        for etat in noeud : 
            liste_grille = [[] for k in range(len(etat))]
            for ligne in range(len(etat)):
                for colonne in range(len(etat[ligne])):
                    liste_grille[ligne].append(etat[ligne][colonne])
    
            #On a obtenu une liste de listes que l'on transforme en grille 
             grille = Grid(len(liste_grille),len(liste_grille[0]),liste_grille)

             #on crée les arrêtes entre deux grilles reliées par un swap horizontal
              for colonne in range(grille.n-1):
                for ligne in range(grille.m):
                    grille2 = grille.copy()
                    grille2.swap((ligne,colonne),(ligne, colonne +1))
                    graph_etats_grille.add_edge(grille.grid_as_tuple(),grille2.grid_as_tuple())
            
            #on fait de même pour deux grilles reliées par un swap vertical 
            for ligne in range(grid.m-1):
                for colonne in range(grid.n):
                    grille2 = grille.copy()
                    grille2.swap((ligne,colonne),(ligne+1,colonne))
                    graph_etats_grille.add_edge(grille.grid_as_tuple(),grille2.grid_as_tuple())

         return graph_etats_grille 


#######
    from intertools import permutations 

    def construire_le_graph(self): 
        # on crée une liste avec toutes les listes de permutations possibles de la grille 
         graph = {}
         grille_ordonnee = [i for i in range(1, self.n*self.m + 1)]
         toutes_les_listes = list(intertools.permutations(grille_ordonnee))

         # on va transformer les listes en grilles 
         for permutation in toutes_les_listes :
            cl = 0 
            num = 0
            for li in range (0,self.m) : 
                while cl < self.n : 
                    self.state[li][cl] = permutation[num] 
                    num = num + 1 
                    cl = cl + 1
                cl = 0
            # on sort de cette boucle avec une grille qui correspond à la liste permutation
            # On ajoute les grilles comme noeuds du graph 
            graph[tuple(map(tuple, self.state))] = [row[:] for row in self.state]

        # on va créer des arrêtes entre deux noeuds si on peut les relier par un swap 
         for node in graph : 
            for li in range(self.m):
                for cl in range(self.n): 
                    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # on peut aller dans 4 directions : droite bas gauche haut 
                        ni, nj = li + di, cl + dj
                         while 0 <= ni < self.m and 0 <= nj < self.n : # on vérifie que l'on est pas au bord de la grille 
                        # Effectuer un coup de swap entre les nombres à la position (i, j) et (ni, nj)
                             new_state = tuple(map(tuple, self.swap(li, cl, ni, nj)))
                             noeud_correspondant = graph[new_state]
                             graph[node].append(noeud_correspondant) 
        
         return graph 


    
    
        




    