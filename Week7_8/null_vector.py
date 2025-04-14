'''
The program creates a null vector of length 10 where the value at fifth position is 1.
'''
import numpy as np

vector = np.zeros(10, dtype=int)
vector[4] = 1

print("The null vector is\n",vector)
#print(__doc__)
