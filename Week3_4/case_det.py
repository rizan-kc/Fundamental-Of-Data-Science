'''
The program takes string as input and counts the number of uppercase letters and lowercase letters.
'''
def case_counter(string):
    '''
    Counts the number of lowercase and uppercase letters in a string

    Parameters:
    string : to analyze

    Returns the number of lower case and uppercase letters.

    '''
    upper_counter = 0
    lower_counter = 0
    for i in string:
        if i.isupper():
            upper_counter += 1
        elif i.islower():
            lower_counter += 1
    return upper_counter, lower_counter
            
string = input("Enter a string: ")
x,y = case_counter(string)
print(f"The number of uppercase characters is {x} and lowercase characters is {y}.")