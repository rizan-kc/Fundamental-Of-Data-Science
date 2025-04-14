'''
This program creates an array of random integer numbers, then sorts and performs different operations
such as reshaping it into different possible dimension.
'''
import numpy as np

#Array creation using 10 random integers from 0 to 99(included)
arr_int = np.random.randint(100,size=10,dtype=int)
print()
print("Original array:")
print(arr_int)
print()

#Sorting the array
sort_arr = np.sort(arr_int)
print("Sorted Array: ")
print(sort_arr)
print()

#Reshaping the array into 1 rows and 10 columns
arr2r5c = sort_arr.reshape(2,5)
print("Reshaped to 2 rows and 5 columns:")
print(arr2r5c)
print()

#Reshaping the array into 1 rows and 10 columns
arr5r2c = sort_arr.reshape(5,2)
print("Reshaped to 5 rows and 2 columns:")
print(arr5r2c)
print()