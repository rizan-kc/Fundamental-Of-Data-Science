'''
The program display whether the number entered is even or odd.
'''
# Taking input from the user
num = int(input("Enter any number: ")) 
# Checking if the number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")