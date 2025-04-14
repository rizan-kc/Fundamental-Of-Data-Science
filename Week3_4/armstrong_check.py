'''
The program checks whether the given number is Armstrong or not.
'''      
def armstrong_detector(n):
    '''
    Checks if the number is armstrong or not.

    Parameters:
    n: A number to analyze.

    Returns "Armstrong" if n is a prime otherwise "not an Armstrong".
    '''
    string = str(n)
    digit = len(string) #returns the no of digits
    
    lst = list(string)
    s = 0
    for i in lst:
        p = int(i) ** digit
        s = s + p 
    print(s)
    if s == n:
        return "Armstrong."
    else:
        return "not Armstrong."

#print(__doc__)
number = int(input("Enter the number: "))
result = armstrong_detector(number)
print(f"The number {number} is {result}")
