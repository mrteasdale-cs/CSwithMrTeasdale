## Dress Sizes
## Program 58
## With Comments

## The program starts by creating an empty list to store the Dress Sizes.
dresses = []

## The program should now loop until the user enters 999 as a dress size.
size = 0
while size !=999:
    ## Ask the user for the two inputs (add/remove and dress size)
    choice = str(input("Do you wish to add (A) or remove (R) a dress?"))
    ## validate the input as only two choices should be entered
    while not(choice.upper()=="A" or choice.upper()=="R"):
        choice = str(input("Please enter only A or R"))

    size = int(input("Please enter a new dress size"))

    ## Add or remove a dress if size is not 999.
    if size !=999:
        if choice.upper() == "A":
            dresses.append(size)
        else:
            dresses.remove(size)
        print("Stock = ",dresses)
## Using the max and min functions display the required output.
print("The largest dress in stock is size",max(dresses))
print("The smallest dress in stock is size",min(dresses))
