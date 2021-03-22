## Guess the Number
## Program 43
## With Comments

## First the program has to store the answer and a default
## value for the users guess.

answer = 37
guess = 0

print("Guess the hidden number between 1 and 100")
## The loop stops when the users guess is equal to the answer.
while answer != guess:
    guess = int(input("Enter your guess."))

    ## A second loop is used to validate that the guess is between 1 and 100
    while guess<1 or guess>100:
        print("Your guess was not valid. Enter it again.")
        guess = int(input("Enter your guess."))

    ## A complex if statements is used to inform the user of whether
    ## their guess was correct, too high or too low.
    if answer == guess:
        print("Correct! Well Done")
    elif guess < answer:
        print("Your guess is too low. Try again")
    else:
        print("Your guess is too high. Try again")
