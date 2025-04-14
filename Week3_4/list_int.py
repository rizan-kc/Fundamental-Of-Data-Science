'''
This program prompts the user for a series of integers, stores only those values in a list
which are in between 1 to 100 and displays the list.
'''
#print(__doc__)
num_list = list()
while 1:
    n = int(input("Enter the number: "))
    if 1 <= n <= 100:
            num_list.append(n)
    ch = input("Enter 'y' to add more number and 'n' to stop: ")
    if ch == 'y':
        continue
    elif ch == 'n':
        break
    else:
        print("Invalid Choice!")
print(f"The resulting list is {num_list}.")