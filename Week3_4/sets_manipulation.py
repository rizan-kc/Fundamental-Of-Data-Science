'''
This program performs a union of set1 and set2 and stores the result in uni.
Finds and stores the common element between set1 and set2 and stores the result in inter.
Program stores the element that are in either of the sets set1 and set2 but not in both.
Program adds an element 40 to the set1.
Program removes an element 20 from set2.
'''
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

uni = set1.union(set2)

print(f"The union of {set1} and {set2} is {uni}.")
print(len(uni))

inter = set1.intersection(set2)
print(f"The intersection of {set1} and {set2} is {inter}.")


sym_diff = set1.symmetric_difference(set2)
print(f"The symmetric difference between {set1} and {set2} is {sym_diff}.")

set1.update({40})
print(f"Set1 after adding element 40 is {set1}.")

set2.remove(20)
print(f"Set2 after removing element 20 is {set2}.")