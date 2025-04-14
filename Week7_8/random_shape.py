'''
The program prompts user to input two numbers a and b. a represents rows and b represents columns.
Then, the program creates an array containing random elements of the shape based on the input a and b.
The program prints the array and average of the array.
'''
import numpy as np

a = int(input("Enter the number of rows: "))
b = int(input("Enter the number of columns: "))

arr = np.random.randint(1, 1000,size=(a,b),dtype=int)
print(f"The array of {arr.shape} is: \n {arr}")

arr1 = arr.ravel()
s = 0
for i in arr1:
    s += i
avg = s/len(arr1) 
print(f"The average of array is {avg}.")