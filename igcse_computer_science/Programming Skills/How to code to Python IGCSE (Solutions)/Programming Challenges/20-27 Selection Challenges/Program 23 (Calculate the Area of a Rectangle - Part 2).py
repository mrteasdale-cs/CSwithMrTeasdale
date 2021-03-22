## Calculating the Area of a Rectangle (Part 2)
## Program 23
## with comments

## The user is asked for two inputs (length and width) for
## both rectangles.

print ("Rectangle 1")
length1 = int(input("Please enter the length:"))
width1 = int(input("Please enter the width:"))

print ("Rectangle 2")
length2 = int(input("Please enter the length:"))
width2 = int(input("Please enter the width:"))

## The length and width are then multiplied together for each
## rectangle.

area1 = length1 * width1
area2 = length2 * width2

## An if statement is used to decide which rectangle is largest
## and display the result.

if area1 > area2:
    print ("Rectangle 1 has the largest area")
else:
    print ("Rectangle 2 has the largest area")


## Note regarding the two sets of inputs.
## Note that different variable names must be used for each.
## rectangle.  If the same variables are used the width and
## length of the second rectangle will overwrite the values
## stored for the first rectangle.