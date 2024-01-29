from grid import Grid

"Idée: partir de la case et trouver le chiffre qui doit y être"
"Coder un truc du style i*m + l'indice de la colonne (double boucle for?)"

class Solver(): 
    """
    A solver class, to be implemented.
    """
    
    def get_solution(self):
        for k in range (1, self.n*self.m + 1):
            i = 0
            j = 0 
            v = 0
            u = 0
            cl = 0
            while state[i][j] != k : 
                if j < self.n - 1 : 
                    j=j+1
                elif j == self.n-1 :
                    j=0 
                    i = i + 1 

            

            # on trouve la ligne sur laquelle le nombre k doit être 
            while k> self.n : 
                v = k - self.n 
                cl += 1 
                return cl 
    
            # on met le nombre k sur la bonne ligne 
            while i != cl : 
                if i < cl : 
                    self.swap((i,j),(i+1, j))
                    i = i+1
                elif i > cl :
                    self.swap ((i,j),(i-1, j))
                    i=i-1



        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

