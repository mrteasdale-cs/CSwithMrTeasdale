## Advice Please (Part 2)
## Program 25
## With comments

## The user is asked to input the answer to a question:

advice = str(input("Would you like some advice?"))

## The program now makes a decision.
## If the user enters 'Y' or 'N' the program should display a messgage.

if advice == "Y":
    print ("Always know where your towel is.")

if advice == "N":
    print ("So long, and thanks for all the fish.")

## Any input (other than Y or N) should result in a different
## message being displayed.

if advice != "Y" and advice !="N":
    print ("Sorry, you were asked to enter Y or N.")

## The 'and' operator is used because we want both parts of the
## condition to be true (not Y AND not N) before the second
## message is displayed.