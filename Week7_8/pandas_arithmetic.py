'''
This program performs different operation over two Pandas Series such as Addition, Subtraction, Multiply 
and division.
'''
import pandas as pd

list1 = [10,20,30,40,50]
list2 = [2,3,4,5,6]
s1 = pd.Series(list1)
s2 = pd.Series(list2)
print("The series 1 is:\n",s1)
print("The series 2 is:\n",s2)

addition_result = s1 + s2
print("Addition result:\n",addition_result)

sub_result = s1 - s2
print("Subtraction result:\n",sub_result)

multiply_result = s1 * s2
print("Multiplication result:\n",multiply_result)

division_result = s1 / s2
print("Division result:\n",division_result)