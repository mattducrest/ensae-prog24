from grid import Grid
import random
import heapq
import copy

"Cette solution très brutale fonctionne jusqu'a des matrice de taille 3*3. Sur mon pc il faut environ 3 secondes en moyenne pour"
"ordonner une matrice 3*3. Pour une matrice 4*4 à part coup de chance majeur il faudrait environ 5 heures. Il est indéniable que cette fonction"
"solveur fonctionne, mais le temps pour résoudre le problème peut être long pour des grandes matrices"

class SolverRandom():

    def __init__(self, m, n, initial_state=[]):
        super().__init__(m, n, initial_state)


    def get_solution(self):
        # Perform random swaps until the matrix is sorted
        sequence = [] #liste des swaps effectués
        swaps = 0 #nombre de swaps
        while not self.is_sorted():
            # Select two random indices for the swap, ensuring no diagonal swaps
            i1, j1 = random.randint(0, self.m - 1), random.randint(0, self.n - 1)
            if random.choice([True, False]):  # Vertical swap if possible
                i2 = i1 + random.choice([-1, 1]) if (i1 > 0 and i1 < self.m - 1) else (i1 - 1 if i1 == self.m - 1 else i1 + 1)
                j2 = j1
            else:  # Horizontal swap if possible
                j2 = j1 + random.choice([-1, 1]) if (j1 > 0 and j1 < self.n - 1) else (j1 - 1 if j1 == self.n - 1 else j1 + 1)
                i2 = i1
            
            # Perform the swap
            self.swap((i1, j1), (i2, j2))
            sequence.append(((i1,j1), (i2,j2)))
            swaps += 1
        
        print(sequence)
        print(f"Total number of swaps: {swaps}") 
        return sequence #j'ai remplacé return self par return sequence
    
    """
    Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
    """

sequence_swaps=[] #global variable

"Une solution bien meilleur qui consiste à chercher chaque nombre dans l'ordre croissant et le mettre où il doit être dans la grille"
class SolverSearch(): 
    def __init__(self, m, n, initial_state):
        self.grid = Grid(m, n, initial_state)
        self.n = n
        self.m = m

    def find_coordinates_x(self, grid, x:int):
        """
        Get the cell's coordinates (i,j) of an integer

        Parameters: 
        -----------
        grid
            The grid.
        x: int
            An integer from the grid.

        Output: 
        -------
        (i,j): tuple[int]
            The integer's cell coordenates.
        """
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == x: 
                    return (i, j)
    
    def drag_x(self, x):
        (i, j) = self.find_coordinates_x(self.grid.state, x) # (i,j) coordonnée de x dans la matrice non ordonnée
        correct_matrix = Grid(self.m, self.n) # Without initial state in order to get a sorted matrix
        i_target, j_target = self.find_coordinates_x(correct_matrix.state, x)
        while j != j_target: # On se place dans la meme colonne que la place objectif
            if j_target < j:
                for k in range(j - j_target):
                    sequence_swaps.append(((i, j), (i, j - 1)))
                    self.grid.swap((i, j), (i, j - 1))
                    j = j - 1
            else:
                for k in range(j_target - j):
                    sequence_swaps.append(((i, j), (i, j + 1)))
                    self.grid.swap((i, j), (i, j + 1))
                    j = j + 1
        while i != i_target: # On remonte droit vers l'objectif pour ne pas déranger ce qui a été fait
            for k in range(i - i_target):
                sequence_swaps.append(((i, j), (i - 1, j)))
                self.grid.swap((i, j), (i - 1, j))
                i = i - 1

        current_state = Grid(self.m, self.n, self.grid.state)
        if current_state != correct_matrix:
            print(f"Current state after dragging {x}:")
            print(current_state)
    
    def get_solution(self):
        for x in range(1, self.m * self.n + 1):
            self.drag_x(x)
        return sequence_swaps
    


"""

Première méthode que l'on a essayée mais qui ne fonctionne pas : 
 def get_solution(self):
        sequence = []
        swaps = 0

        for i in range (0, self.m): 
            for j in range(0, self.n): 
                if  i < self.m-1 and self.state[i][j] > self.state[i+1][j]: # on regarde si la case est plus grande que celle diretement en dessous
                    self.swap((i,j),(i+1, j)) # si elle est plus grande on swap
                    sequence.append(((i,j),(i+1, j))) 
                    swaps = swaps + 1

                if  j < self.n -1 and self.state[i][j] > self.state[i][j+1]: # on regarde dans l'ordre des cases si elles sont plus grandes que la case à leur droite
                    self.swap((i,j),(i, j+1)) # si elle est plus grande on swap
                    sequence.append(((i,j),(i, j+1))) # on prend note des deux cellules qu'on a swap
                    swaps = swaps + 1 # on incrément le compteur du total des swaps

                
                if self.state[((i+1)*self.n)+1][0] < ((i+1)*self.n+1) and i < self.m-1:
                   self.swap((((i+1)*self.n)+1),0),(i*self.n,0)
                   sequence.append((((i+1)*self.n+1,0),(i*self.n+1, 0)))
                   swaps = swaps + 1 # on incrément le compteur du total des swaps

        print(sequence) 
        print(f"Total number of swaps: {swaps}") 
        return self

    "La fonction get_solution ne fonctionne pas. L'idée est d'ordonner les coordonnées par lignes et par colonnes."
    "Ceci ne fonctionne pas parce que certaines coordonnées peuvent être 'coincées' à gauche. Par example, la fonction dit que la matrice:"
    " [[1,3,4], [2,5,6]] est ordonnée. En effet elle l'est si on ne regarde que les lignes et les colonnes.  Mais on ne peut pas déplacer le 2"
    "Parce qu'il est plus grand que 1 et plus petit que 5, on est donc coincés"
    """ 


"""implémentation de A*

      paramètres: 
        -----------
        grid: Grid
            la grille d'origine

        image: 
        -------
        chemin : liste de listes
""" 
@staticmethod
def A_star(grid):
    Solution = Grid(grid.m, grid.n).grilles_comme_tuples() 
    Queue = [(0,grid.grilles_comme_tuples())] 
    """initialise une liste prioritaire et la grille de départ. Cette liste prioritaire va permettre
    de choisir le chemin le plus court
    """
    visites = [] 
    Parent = dict() #dictionnaire qui va permettre de retracer le chemin réalisé
    soltion_trouvee = False #la solution a t'elle été trouvée ?

    while Queue != [] and not(soltion_trouvee) :#tant que la queue n'est pas vide et que l'on a pas trouvé la solution 
            
        grille_actuelle = heapq.heappop(Queue) 
        """récupère et retire de la queue le tuple qui représente la grille actuelle et le chemin le plus court
        parcouru jusqu'à présent """
        grille_actuelle = grille_actuelle[1] #on extrait la grille en question

        if grille_actuelle not in visites:
            visites.append(grille_actuelle) #on a visité la grille actuelle 
                
            # On transforme la grille actuelle qui est sous forme de tuple en liste de listes 
            L = []
            for k in grille_actuelle :
                L.append(list(k)) 
                
            grilles_a_venir = Grid(len(L),len(L[0]),L).grilles_adjacentes() 
            #toutes les grilles adjacentes à la grille actuelle et l'action nécessaire pour passer de l'une à l'autre
                
            for (N,swap) in grilles_a_venir:

                # pour chaque grille adjacente on la transforme en liste de listes
                NL = []
                for k in N: #k est un tuple qui représente une ligne de la grille
                    NL.append(list(k))

                if N not in Parent.keys(): #si on n'a pas encore visité la grille
                    Parent[N] = (grille_actuelle,swap) #on l'ajoute au dictionnaire la grille N et le chemin parcouru 
                    heapq.heappush(Queue, (len(SolverRandom.get_solution(Grid(len(NL),len(NL[0]),NL))),N)) 
                    #ajouter de nouveaux états à la grille tout en maintenant l'ordre de priorité
                    
                if N == Solution:
                    soltion_trouvee = True
        
    chemin = []
    N = Solution
    while N != grid.grilles_comme_tuples(): 
    #tant que la solution n'est pas la grille initiale 
        N,swap = Parent[N] #on récupère le parant de la grille actuelle et le swap associé
        chemin.append(swap) #on rajoute le swap au chemin
        chemin.reverse() #on remet le chemin dans l'ordre
    return chemin

@staticmethod
def A_star2(grid):
    Solution = Grid(grid.m, grid.n).grilles_comme_tuples() 
    Queue = [(0,grid.grilles_comme_tuples())] 
    """initialise une liste prioritaire et la grille de départ. Cette liste prioritaire va permettre
    de choisir le chemin le plus court
    """
    visites = [] 
    Parent = dict() #dictionnaire qui va permettre de retracer le chemin réalisé
    soltion_trouvee = False #la solution a t'elle été trouvée ?

    while Queue != [] and not(soltion_trouvee) :#tant que la queue n'est pas vide et que l'on a pas trouvé la solution 
            
        grille_actuelle = heapq.heappop(Queue) 
        """récupère et retire de la queue le tuple qui représente la grille actuelle et la taille du chemin le plus court
        parcouru jusqu'à présent """
        grille_actuelle = grille_actuelle[1] #on extrait la grille en question

        if grille_actuelle not in visites:
            visites.append(grille_actuelle) #on a visité la grille actuelle 
                
            # On transforme la grille actuelle qui est sous forme de tuple en liste de listes 
            L = []
            for k in grille_actuelle :
                L.append(list(k)) 
                
            grilles_a_venir = Grid(len(L),len(L[0]),L).grilles_adjacentes() 
            #toutes les grilles adjacentes à la grille actuelle et l'action nécessaire pour passer de l'une à l'autre
                
            for (N,swap) in grilles_a_venir:

                # pour chaque grille adjacente on la transforme en liste de listes
                NL = []
                for k in N: #k est un tuple qui représente une ligne de la grille
                    NL.append(list(k))

                if N not in Parent.keys(): #si on n'a pas encore visité la grille
                    Parent[N] = (grille_actuelle,swap) #on l'ajoute au dictionnaire la grille N et le chemin parcouru 
                    heapq.heappush(Queue, (len(SolverSearch.get_solution(SolverSearch(len(NL),len(NL[0]),NL))),N)) 
                    #ajouter de nouveaux états à la grille tout en maintenant l'ordre de priorité 
                    
                if N == Solution:
                    soltion_trouvee = True
        
    chemin = []
    N = Solution
    while N != grid.grilles_comme_tuples(): 
    #tant que la solution n'est pas la grille initiale 
        N,swap = Parent[N] #on récupère le parant de la grille actuelle et le swap associé
        chemin.append(swap) #on rajoute le swap au chemin
        chemin.reverse() #on remet le chemin dans l'ordre
    
    return chemin



