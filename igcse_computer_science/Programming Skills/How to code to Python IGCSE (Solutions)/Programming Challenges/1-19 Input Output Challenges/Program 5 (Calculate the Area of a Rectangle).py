## Calculating the Area of a Rectangle
## Program 5
## with comments

## The input box shows that a message is first given to the user so a print()
## statement is required at the beginning of the program.
## The user is then asked for 2 inputs (length and width).

print ("Please enter the following values in cm")
length = int(input("Please enter the length of the rectangle"))
width = int(input("Please enter the width of the rectangle"))


## The length and width are then multiplied together to calculate the area.
## To store the answer requires a third variable which we have called 'area'.

area = length * width

## Finally the result of the calculation is displayed.

print ("The area of the rectangle is:")
print (area,"square centimetres")