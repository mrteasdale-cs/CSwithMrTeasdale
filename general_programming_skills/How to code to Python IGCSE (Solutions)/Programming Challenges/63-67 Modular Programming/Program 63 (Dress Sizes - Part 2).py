## Dress Sizes (part 2)
## Program 63
## With Comments

## The function below is passed a value and a list.  It counts how
## often the value appears in the list and returns this total.
def numberInList(value,theList):
    countsize = 0
    for loop in range(len(theList)):
        if  theList[loop] == value:
            countsize += 1
    return countsize


dresses = []

size = 0
while size !=999:
    choice = str(input("Do you wish to add (A) or remove (R) a dress?"))
    while not(choice.upper()=="A" or choice.upper()=="R"):
        choice = str(input("Please enter only A or R"))
    size = int(input("Please enter a new dress size"))

    if size !=999:
        if choice.upper() == "A":
            dresses.append(size)
        else:
            dresses.remove(size)
        print("Stock = ",dresses)

## Ask the user to select a dress size and pass the result to the function.
selectedSize = int(input(("Enter a dress size to count:")))
numDress = numberInList(selectedSize,dresses)
print("There are",numDress,"size",selectedSize,"dresses in stock")

print("The largest dress in stock is size",max(dresses))
print("The smallest dress in stock is size",min(dresses))

## Note: Functions are often written to be used over and over again.
## The function above does not use variable names related to the problem
## like 'dress' or 'size' as it simply counts a values appearance in any
## list.
## Keeping the function generic means it could be inserted into another
## program to accomplish the same task.
