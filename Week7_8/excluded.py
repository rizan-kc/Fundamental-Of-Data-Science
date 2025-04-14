'''
The program creates an array of size 10 where elements ranges from 0 to 1 where 0 and 1 are excluded.
'''
import numpy as np

arr = np.linspace(0,1,12)[1:-1]
print("The array is:\n",arr)