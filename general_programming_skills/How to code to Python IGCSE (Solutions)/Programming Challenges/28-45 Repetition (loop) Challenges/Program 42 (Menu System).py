## Menu System
## Program 42
## With Comments

## The program itself is a simple loop.  The complexity of this
## program is in the complexity of the condition in the loop.

selection = ""

while selection != "Q" and selection != "A" and selection != "K" and selection != "L":
    selection = str(input("Enter your menu choice (Q, A, K or L)"))
    selection = selection.upper()

    ## An error message is generated using an if statement to display a message
    ## if the user does not give a valid input.
    ## Note:
    ## The condition of the if statement required to generate the error message
    ## should be the same as the while loop.  For variety the if statement
    ## below once agaiin demonstrates that the same condition can be written
    ## in several ways.
    if not(selection=="Q" or selection == "A" or selection == "K" or selection == "L"):
        print(selection,"is not valid. Enter Q, A, K or L")

## The print statement below is only displayed when the program exits
## the above loop.
print(selection,"selected")