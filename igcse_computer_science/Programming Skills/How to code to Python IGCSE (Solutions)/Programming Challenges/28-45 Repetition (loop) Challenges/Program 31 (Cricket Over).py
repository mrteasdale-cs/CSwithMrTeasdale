## Cricket Over
## Program 31
## With Comments

## A total variable is set to 0.  This will be used later.
## An initial message is displayed:

total = 0
print("Please enter the score for each ball.")

## In this challenge an input is placed inside a loop.
## The loop repeats the following 6 times
##   - the user is asked for an input (ball score)
##   - each input is added onto the total.

for loop in range(6):
    ball = int(input())
    total = total + ball

## A message with the final total is displayed.

print("This over’s score was:",total)