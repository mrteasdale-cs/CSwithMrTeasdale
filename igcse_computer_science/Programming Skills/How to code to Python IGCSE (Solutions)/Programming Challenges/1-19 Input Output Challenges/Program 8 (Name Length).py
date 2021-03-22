## Name Length
## Program 8
## with comments

## The user is prompted to type in a forename and surname.

forename = str(input("Please enter your forename:"))
surname = str(input("Please enter your forename:"))

## The len() function is used to calculate the number of
## characters stored in the forename and surname variables.

letters = len(forename+surname)

## The number of characters, now stored in the letters variable
## are displayed as part of a message.

print ("There are",letters,"letters in your name.")

## NOTE
## The last two lines of the program could be combined.
##    print ("There are",len(forename+surname),"letters in your name.")