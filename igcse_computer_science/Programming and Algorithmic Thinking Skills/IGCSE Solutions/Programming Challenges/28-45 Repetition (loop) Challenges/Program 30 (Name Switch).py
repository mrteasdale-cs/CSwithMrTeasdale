## Name Switch
## Program 30
## With Comments

## The user is asked to input their first name and surname:

first = str(input("Please enter first name:"))
sur = str(input("Please enter surname:"))

## Every other line of the output is different.  This means that
## to repeat the pattern there must be two print statements inside
## the loop.

for loop in range(3):
    print (first[:1],sur[:1],first.upper(),sur.lower(),first+sur)
    print (first+sur,sur.upper(),first.lower(),sur[:1].lower(),first[:1].lower())

## NOTE
## To get the correct pattern each print statement is built using
## sub-string to extract letters, concatenation to join strings
## and upper/lower to change the case of the strings.
