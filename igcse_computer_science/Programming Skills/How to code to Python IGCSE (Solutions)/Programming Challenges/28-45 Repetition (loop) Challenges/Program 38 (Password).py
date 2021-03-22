## Password
## Program 38
## With Comments

## The password is stored in a variable.

password = "ornery"

## This program uses a while loop.
## This will keep repeating while the users input is not equal to the password.

guess = str(input("Please enter the password."))
while guess != password:
    print("Sorry, incorrect! Try again.")
    guess = str(input("Please enter the password."))

## The print statement below is only displayed when the program exits
## the above loop.
print("Entry gained!")