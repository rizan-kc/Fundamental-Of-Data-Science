'''
The program to find the Euclidean distance between two 
coordinates. Take both the coordinates from the user as input.
'''
# Taking coordinates input from the user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Euclidean distance formula
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# Displaying result
print(f"Euclidean Distance: {distance}")
