'''
The program creates a 5x5 matrix values ranging from 0 to 4.
'''
import numpy as np

x = np.arange(5)
matrix = np.tile(x,(5,1))

print("The 5X5 matrix containing values from 0 to 4 is:\n",matrix)
