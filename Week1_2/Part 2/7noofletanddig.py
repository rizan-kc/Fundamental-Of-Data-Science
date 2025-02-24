'''
The program accepts a string and calculates the number of digits and letters.
'''
# Taking input from the user
string = input("Enter anything: ")
letter_count = 0
digit_count = 0
# Iterating through each character in the string
for char in string:
    if char.isalpha():  # Checks if character is a letter
        letter_count += 1
    elif char.isdigit():  # Checks if character is a digit
        digit_count += 1
# Displaying the results
print(f"The number of letters is {letter_count}.")
print(f"The number of digits is {digit_count}.")

