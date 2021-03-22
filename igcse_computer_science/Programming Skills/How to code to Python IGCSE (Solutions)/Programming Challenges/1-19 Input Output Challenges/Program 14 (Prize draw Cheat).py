## Prize Draw Cheat
## Program 14
## with comments

## The user should be asked to enter two float numbers.

jarVol = float(input("Please enter the volume of the jar (cm3):"))
sweetVol = float(input("Please enter the volume of one sweet (cm3):"))

## To calculate the number of sweets divide one volume by the other.

sweets = jarVol/sweetVol

## The number of sweets should be rounded down to the nearest
## whole sweet using the int() function.
## This could be done when calculating the sweets above
##      sweets = int(jarVol/sweetVol)
## or when displaying the answer as shown below.

print (int(sweets),"sweets fit into the jar.")