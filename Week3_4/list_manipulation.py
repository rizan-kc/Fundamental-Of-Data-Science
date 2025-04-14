'''
This program prompts the user to enter integer values to populate two lists, then prints messages like:
- Whether the lists are of the same length.
- Whether the elements in each list sum to the same value.
- Whether there are any values that occur in both lists
'''
num_list1 = []
num_list2 = []
s1 = 0
s2 = 0
c = 0

# For first list and second list
while 1:
    n1 = int(input("Enter the number for first list: "))    
    num_list1.append(n1)
    s1 = s1 + n1
    ch1 = input("Enter y to add more number and n to stop: ")
    if ch1 == 'y':
        continue
    elif ch1 == 'n':
        break

print()

while 1:
    n2 = int(input("Enter the number for second list: "))    
    num_list2.append(n2)
    s2 = s2 + n2 
    ch2 = input("Enter y to add more number and n to stop: ")
    if ch2 == 'y':
        continue
    elif ch2 == 'n':
        break
print()
print(f"The first list is {num_list1} and second list is {num_list2}.")

# a) the lists are of the same length.
if len(num_list1) == len(num_list2):
    print("Both list are of same length!")
else:
    print("The lists are of different length!")

# Whether the elements in each list sum to the same value.
if s1 == s2:
    print("Elements of both the lists sum to the same value.")
else:
    print("Elements of both the lists does not sum to the same value.")

# Whether there are any values that occur in both lists
for i in num_list1:
    for j in num_list2:
        if i == j:
            print(f"{i} is the value that occurs in both the list.")