## Leftover Paint
## Program 15
## with comments

## This program uses the ceil() function so maths must be imported.
import math

## The user should be asked to enter two float numbers.

area = float(input("Enter the area in m2 to be painted."))
paintPot = float(input("Enter the area (m2) that a single pot covers."))

## To calculate the number of pots divide one value by the other.

pots = area/paintPot

## This value should be rounded up to the nearest
## whole pot using the ceil() function.

pots = math.ceil(pots)

## To work out the remaining paint the modules of area/paintPot.
## can be calculated.

remaining = area%paintPot

## The results can then be displayed.
print ("You will need",pots,"pots of paint.")
print ("You can paint",remaining,"m2 with the leftover paint.")