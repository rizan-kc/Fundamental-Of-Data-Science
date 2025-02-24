'''
The program prints the number which are divisible by 7 and multiple of 5 
between 1500 and 2000 (both included).
'''
print("Number divisible by 7 and multiple of 5 between 1500 and 2000(both included):")
for x in range(1500,2001):
    if x % 7 == 0 and x % 5 == 0:
        print(x)
