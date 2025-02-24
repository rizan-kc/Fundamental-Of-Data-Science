'''
The program is a simple number guessing game where the user has 5 attempts 
to guess a randomly generated number.
'''
import random
#Generating a random number between 1 and 100
answer = random.randint(1,100)
attempts = 5 # Maximum attempts allowed

print(format('Welcome to the Number Guessing Game!','>50'))
for x in range(1,attempts + 1):
    guess = int(input("Enter any number: "))
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print("Correct number")
        break
    if x == attempts: 
        print(f"Game Over, The number was {answer}.")