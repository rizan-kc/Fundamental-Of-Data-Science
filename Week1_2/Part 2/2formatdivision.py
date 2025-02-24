''' 
Program prompts the user for two integer values and display the results 
of the first number divided by the second, with exactly two decimal places 
displayed.
'''
first_number = int(input("Enter any number: "))
second_number = int(input("Enter any number: "))
#Error Handling
if second_number == 0:
    print("Error! Division by zero is invalid.")
else:
    result= first_number / second_number
    print(f"Result: {result:.2f}")

