## Calculating the Area of a Circle
## Program 13
## with comments

## The input box shows that a message is first given to the user so a print()
## statement is required at the beginning of the program.
## The user is then asked for 1 input (radius).

print ("Please enter the following values in cm")
radius = int(input("Please enter the radius of a circle"))


## To calculate the area of a circle the radius should be
## squared using the pow() function.

area = 3.14 * pow(radius,2)

## Finally the result of the calculation is displayed.

print ("The area of the circle is:")
print (area,"square centimetres")