from grid import Grid

"Idée: partir de la case et trouver le chiffre qui doit y être"
"Coder un truc du style i*m + l'indice de la colonne (double boucle for?)"

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
        print(swaps) 
        return self


     
"""    def get_solution(self):
        sequence = []
        swaps = 0

        for j in range (0, self.m): 
            for i in range(0, self.n): 
                print(self.state[i][j+1])
                if  j < self.m -1 and self.state[i][j] > self.state[i][j+1]: # on regarde dans l'ordre des cases si elles sont plus grandes que la case à leur droite
                    self.swap((i,j),(i, j+1)) # si elle est plus grande on swap
                    sequence.append((i,j),(i, j+1)) # on prend note des deux cellules qu'on a swap
                    swaps = swaps + 1 # on incrément le compteur du total des swaps
                
                if  i < self.n-1 and self.state[i][j] > self.state[i+1][j]: # de même on regarde si la case est plus grande que celle diretement en dessous
                    self.swap((i,j),(i+1, j)) # si elle est plus grande on swap
                    sequence.append((i,j),(i+1, j)) 
                    swaps = swaps + 1

        print(sequence) 
        print(swaps) 
        return self

        """


"""
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
  

