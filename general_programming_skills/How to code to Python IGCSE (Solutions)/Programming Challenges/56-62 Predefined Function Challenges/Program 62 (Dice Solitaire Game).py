## Dice Solitaire Game
## Program 62
## With comments

## import the random number module
import random

## create an empty list to store each dice roll and a counter to
## store the number of dice rolls made during the game.
dice = []
count = 0

## The game will finish when one of each dice value (1,2,3,4,5,6)
## is in the list.  At this point the list will be six elements long.
while not(len(dice)==6):
    count += 1

    ## Simulate a dice roll by generating a random integer from 1-6.
    roll = random.randint(1,6)
    print("Dice rolled =",roll)
    ## Loop through the current list to see if the dice vale rolled
    ## already exists in the list.  A Boolean stores the result.
    found = False
    for loop in range(len(dice)):
        if dice[loop] == roll:
            found = True

    ## If that dice value is already in the list, remove it from the list.
    ## If it is not in the list then add it to the list.
    if found:
        dice.remove(roll)
    else:
        dice.append(roll)
    print(dice)

    ## Display the current list.
    print("After roll",str(count)+":",dice)

## Display the final message.
print("Game completed in",count,"rolls of the dice.")

## Note that this program could easily be changed to have user input
## instead.  User could roll an actual dice and enter the number they
## rolled.

