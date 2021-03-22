## Guess the Number - Part 2
## Program 56
## With Comments

## To create a random number the 'random' module library must be imported
import random

## Rather than the answer being hard coded into the program it is now
## set to a random integer between 1 and 100.
answer = random.randint(1,100)

## The remainer of the program is unchanged.
guess = 0

print("Guess the hidden number between 1 and 100")

while answer != guess:
    guess = int(input("Enter your guess."))

    while guess<1 or guess>100:
        print("Your guess was not valid. Enter it again.")
        guess = int(input("Enter your guess."))

    if answer == guess:
        print("Correct! Well Done")
    elif guess < answer:
        print("Your guess is too low. Try again")
    else:
        print("Your guess is too high. Try again")
