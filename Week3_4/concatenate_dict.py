'''
The program creates three dictionaries dic1,dic2, and dic3.

It concatenates all three dictionaries into new one in the variable named nums.
The program also adds a new key value pair to the dictionary nums.
The program removes the third item from nums.
The program sums up all the items present in the dictionary nums.
The program multiplies all the value present in the dictionary nums.
The program also displays the maximum and minimum values in nums.
'''
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
s = 0
m = 1
max_val = None
min_val = None

nums = dic1 | dic2 | dic3
print(f"The resulting dictionary after concatenation is {nums}.")

nums.update({7:70})
print(f"The resulting dictionary after adding key value pair 7 (key) and 70 (value) is {nums}.")

nums[3] = 80
print(f"The resulting dictionary after updating the value of key 3 is {nums}.")

nums.pop(3)
print(f"The resulting dictionary after removing the third item is {nums}.")

for i in nums:
    s = s + nums[i]
print(f"The sum of all items in dictionary is {s}.")

for j in nums:
    m = m * nums[j]
print(f"The multiplication of all items in dictionary is {m}.")

for val in nums.values():
    if max_val is None or val > max_val:
        max_val = val
    if min_val is None or val < min_val:
        min_val = val
print("Maximum value:", max_val)
print("Minimum value:", min_val)