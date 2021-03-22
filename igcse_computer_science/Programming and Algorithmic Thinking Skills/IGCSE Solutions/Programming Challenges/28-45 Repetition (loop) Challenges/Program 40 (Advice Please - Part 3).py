## Advice Please (Part 3)
## Program 40
## With comments


## Input validation, using a while loop, ensures that only entering Y
## will allow the program to move on.
## If statements inside the loop display different messages if
## the user doen't enter Y.

advice = str(input("Would you like some advice?"))
while advice != "Y":
    if advice == "N":
        print("Don't be silly, you definitely want some advice.")
    if not(advice == "Y" or advice == "N"):
        print("You must enter Y or N")
    advice = str(input("Would you like some advice?"))

if advice == "Y":
    print ("Always know where your towel is.")



## No need for this bit of the previous program as it can never be displayed.
##if advice == "N":
##    print ("So long, and thanks for all the fish.")

