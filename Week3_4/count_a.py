'''
This program prompts the user to enter the list of names and stores it, then checks how many 
times does the character a appears in the list.
'''

name_list = list()
a_counter = 0

while True:
    name = input("Enter the name: ")
    name_list.append(name)
    ch = input("Enter y to add more number and n to stop: ")
    if ch == 'y':
        continue
    elif ch == 'n':
        break
  
print(name_list)
string = ''.join(name_list)

for i in string:
    if i == "a":
        a_counter += 1
print(f"The number of times 'a' appears in {name_list} is {a_counter}.")
