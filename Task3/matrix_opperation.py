#this file does matrix opperations
from random import randint as yeet
import numpy as np

#array_generator will generate a square matrix
#where the matrix == n*n
class matrix_generation():
    def __init__(self,n=3,m=3):
        self._row = n
        self._column = m
    
    def get_row(self):
        return self._row
    
    def get_column(self):
        return self._column
    
    def set_row(self,n):
        self._row = n
    
    def set_column(self,m):
        self._column = m

    def random_square_array_generator(self):
        #we will take column and generate a square matrix based on that
        arr_gen = [[]]
        for i in range(self._column):
            arr_gen[0].append(yeet(0,255))
        arr_gen = arr_gen*self._column
        return np.array(arr_gen)
    
    #figure out this later
    '''
    def random_array_generator(self):
        arr_gen = [[]*self._column]
        for x in range(self._row):
            arr_gen[x].append(yeet(0,255))
        return np.array(arr_gen)
    '''

#since we know it returns a numpy array we can use numpy array opperations on the array

matrix = matrix_generation().random_square_array_generator()
print(matrix)
print("\n")
print(matrix.transpose())
