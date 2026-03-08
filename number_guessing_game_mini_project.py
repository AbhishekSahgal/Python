# Mini Project (Important)
# Number Guessing Game

# Program:
# Set a secret number (example 7)
# Ask user to guess
# If correct → "You guessed it!"
# Otherwise → "Try again"

num = int(input("Enter Your Number: "))
secret = 7

if num == secret:
    print("You Guessed it!")
else:
    print("try again!")