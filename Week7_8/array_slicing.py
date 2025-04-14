'''
The program creates an array of numbers by taking input from the user and slice them to get
element between different indexes.
'''
import numpy as np

arr_list = list()

for x in range(10):
    i = int(input("Enter the number: "))
    arr_list.append(i)

arr = np.array(arr_list)

print("The array is:\n",arr)

sort_arr = np.sort(arr)
print("The array after sorting is:\n",sort_arr)

print("The array after slicing it from index 2 to 5 is",sort_arr[2:5])
print("The array after slicing it from index 5 to 8 is",sort_arr[5:8])
print("The array after slicing it from index 2 to 9 is",sort_arr[2:9])
