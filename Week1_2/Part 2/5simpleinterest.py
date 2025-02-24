'''
The program calculates the Simple Interest when the principle, time and 
rate is provided by the user.
'''
P = float(input("Enter the principle amount: "))
T = float(input("Enter the time period: ")) 
R = float(input("Enter the rate of interest: "))
# Simple Interest Formula
SI = (P * T * R) / 100
print(f"The Simple Interest is {SI}.")