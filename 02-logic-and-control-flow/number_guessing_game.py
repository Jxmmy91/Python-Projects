print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
import random
secret_number = random.randint(1, 10)
max_attempts = random.randint(3, 7)
attempts = 1
print(f"You have {max_attempts} attempts to guess the number.")
guessed_number = int(input("enter guessed number"))
while guessed_number != secret_number and attempts < max_attempts:
    if guessed_number < 1 or guessed_number > 10:
     print("Invalid guess! Enter a number between 1 and 10.")
     guessed_number = int(input("Enter another guess: "))
     continue
    elif guessed_number > secret_number :
     print("Too high! Try a lower number.")
    elif guessed_number < secret_number:
     print("Too low! Try a higher number.")
    attempts = attempts + 1 
    guessed_number = int(input("retry guessed number"))
if guessed_number == secret_number:
    print("Congratulations! You guessed the secret number!")
    print(f"You guessed it in {attempts} attempts.")
else:
    print("Game over! You've run out of attempts.")
    print(f"The secret number was {secret_number}.")