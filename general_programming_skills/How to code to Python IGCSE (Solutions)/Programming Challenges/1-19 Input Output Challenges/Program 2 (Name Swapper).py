## Name Swapper
## Program 2
## with comments

## In program 2 the user is asked to type in their name.
## The user is not given a message this time so there is no text inside
## the input() statement.

## Challenge 2 shows the names being entered are shown on two lines.  From this
## diagram we can work out that there should be two input commands.

forename = str(input())
surname = str(input())


## The output is shown on one line so only one print() is required.
## We can swap the name by printing the variables in a different order.

print (surname,forename)

## Note that printing two variables requires a , or + between them.
## A comma will produce the space between the stored names when they are displayed.