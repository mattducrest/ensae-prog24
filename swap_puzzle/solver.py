from grid import Grid
import random


"La fonction get_solution de cette première classe ne fonctionne pas. L'idée est d'ordonner les coordonnées par lignes et par colonnes."
"Ceci ne fonctionne pas parce que certaines coordonnées peuvent être 'coincées' à gauche. Par exemple, la fonction dit que la matrice:"
" [[1,3,4], [2,5,6]] est ordonnée. En effet elle l'est si on ne regarde que les lignes et les colonnes.  Mais on ne peut pas déplacer le 2"
"Parce qu'il est plus grand que 1 et plus petit que 5, on est donc coincés"

class Solver(): 
    """
    A solver class, to be implemented.
    """

    # Méthode 2 : algorithme de tri à bulles 

    def get_solution(self):
        sequence = []
        swaps = 0

        for i in range (0, self.m): 
            for j in range(0, self.n): 
                if  i < self.m-1 and self.state[i][j] > self.state[i+1][j]: # de même on regarde si la case est plus grande que celle diretement en dessous
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

"Cette solution beaucoup plus brutale fonctionne jusqu'a des matrice de taille 3*3. Sur mon pc il faut environ 3 secondes en moyenne pour"
"ordonner une matrice 3*3. Pour une matrice 4*4 à part coup de chance majeur il faudrait environ 5 heures. Il est indéniable que cette fonction"
"solveur fonctionne, mais le temps pour résoudre le problème peut être long pour des grandes matrices"

class SolverRandom(Grid):
    def __init__(self, m, n, initial_state=[]):
        super().__init__(m, n, initial_state)

    def get_solution(self):
        # Perform random swaps until the matrix is sorted
        sequence = []
        swaps = 0
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
        return self


"""
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
  

