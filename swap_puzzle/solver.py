from grid import Grid

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
            while state[i][j] != k : 
                if j < self.n - 1 : 
                    j=j+1
                elif j == self.n-1 :
                    j=0 
                    i = i + 1 

            while k> self.n : 
                v = k - self.n 
            
            while j != v - 1 : 
                if j < v-1 : 
                    self.swap((i,j),(i, j+1))
                    j = j+1
                else :
                    self.swap ((i,j),(i, j-1))
                    j=j-1
            
            

        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

