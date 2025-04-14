'''
The program is a basic calculator where two numbers are taken as input.
User can perform different arithmetic operation like:
A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Truncated division
F. Modulus
G. Exponentiation
'''

def addition(a,b):
    '''
    The function returns the addition of two numbers.

    Parameter:
    a: first number, datatype = int
    b: second number, datatype = int

    Returns the addition a + b.
    '''
    return a + b

def subtraction(a,b):
    '''
    The function returns the subtraction of two numbers.

    Parameter:
    a: first number, datatype = int
    b: second number, datatype = int

    Returns the addition a - b.
    '''
    return a - b

def multiplication(a,b):
    '''
    The function returns the multiplication of two numbers.

    Parameter:
    a: first number, datatype = int
    b: second number, datatype = int

    Returns the multiplication a * b.
    '''
    return a * b
def division(a,b):
    '''
    The function checks if divisor is 0, If the divisor is 0, it retuns invalid division message otherwise returns the division of two numbers.

    Parameter:
    a: Numerator number, datatype = int
    b: Denominator number, datatype = int

    Returns the invalid division if b is 0 otherwise float number a / b.
    '''
    if b == 0:
        return "invalid: Division by zero"
    else:
        return a / b
def truncate_div(a,b):
    '''
    The function checks if divisor is 0, If the divisor is 0, it retuns invalid division message otherwise returns the truncation division of two numbers.

    Parameter:
    a: Numerator number, datatype = int
    b: Denominator number, datatype = int

    Returns the invalid division if b is 0 otherwise integer number a / b.
    '''
    if b == 0:
        return "invalid: Division by zero"
    else:
        return a // b
    
def modulus(a,b):
    '''
    The function checks if divisor is 0, If the divisor is 0, it retuns invalid division message otherwise returns the modulus of numbers.

    Parameter:    
    a: Numerator number, datatype = int
    b: Denominator number, datatype = int

    Returns the invalid division if b is 0 otherwise returns the remainder when a / b i.e a % b.
    '''
    if b == 0:
        return "invalid operation: Division by zero"
    else:
        return a % b
def exponentiation(a,b):
    '''
    The function returns the exponentiation.

    Parameter:
    a: Base number, datatype = int
    b: Exponent number, datatype = int

    Returns the result of a ** b.
    '''
    return a ** b
#print(__doc__) 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Arithmetic Operation you would like to perform: ")

if operation == '+':
    print(f"The addition is {addition(num1,num2)}.")
elif operation == '-':
    print(f"The subtraction is {subtraction(num1,num2)}.")
elif operation == '*':
    print(f"The multiplication is {multiplication(num1,num2)}.")
elif operation == '/':
    print(f"The division is {division(num1,num2)}.")
elif operation == "//":
    print(f"The truncate division is {truncate_div(num1,num2)}.")
elif operation == "%":
    print(f"The modulus is {modulus(num1, num2)}.")
elif operation == '**':
    print(f"The exponentiation is {exponentiation(num1,num2)}.")
else:
    print(f"The {operation} is invalid.")