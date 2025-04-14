'''
This program checks if the number enetered is prime or not.
'''
def prime_detector(n):
    '''
    Checks if the number is prime or not

    Parameter:
    n: an integer value to check

    Returns "prime" if number is prime otherwise "not a prime".
    '''
    counter = 0
    for i in range(1,n+1,1):
        if n % i == 0:
            counter += 1
    if counter == 2:
        return "prime"
    else:
        return "not a prime"
num = int(input("Enter a number: "))
result = prime_detector(num)
print(f"The number {num} is {result}.")
