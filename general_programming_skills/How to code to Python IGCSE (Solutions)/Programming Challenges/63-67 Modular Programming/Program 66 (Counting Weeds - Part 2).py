## Counting Weeds (Part 2)
## Program 66
## With comments

## A function to count and return the values stored in any 2D list.
def count2DList(twoDlist):
    total = 0
    for outer in range(5):
        for inner in range(5):
            total = total + twoDlist[outer][inner]
    return total

def displayResults(twoDlist,total):
    ## Display the quadrat 2D list.
    for outer in range(5):
        for inner in range(5):
            print(quadrat[outer][inner],"",end=' ')
        print()

    ## Display the total number of weeds.
    print("The total number of weeds found was -",total)

    ## Display an appropriate message for the total number of weeds found.
    if total < 2:
        print("You have a great, well looked after lawn.")
    elif total >= 2 and total <=10:
        print("A bit of light weeding will help your lawn look great.")
    elif total > 10 and total <50:
        print("Your lawn should be treated with an environmentally friendly weed killer.")
    elif total >= 50:
        print("We would advise that your lawn is dug up and re-laid.")



## Main Program

## Declare a 2D list of integers with 5 by 5 elements.
quadrat = [[0] * 5 for main in range(5)]

## Begin by inputting the number of weeds as before.
for outer in range(5):
    for inner in range(5):
        quadrat[outer][inner] = int(input("Please enter the number of weeds counted at "+str(outer+1)+","+str(inner+1)+":"))

## Call a function to sum the values entered into the 2D list and store
## the total returned by the function.
weedTotal = count2DList(quadrat)

## Call a procedure to display the results.
displayResults(quadrat,weedTotal)

## ----- Extension Task ------
## Allow the user to enter the number of squares in the quadrat (length and width).
## Pass these values to a function which creates a quatrat the correct size,
## inputs the number of weeds and returns a 2D list od values.
## The remaining program should be unchanged.
