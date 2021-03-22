## Laying Bricks
## Program 16
## With comments

## The user is asked to input the length of a brick and the length
## of a wall:

## NOTE - Float variables must be used as we do not know if the
## user will enter a whole number or not.

brick = float(input("Please enter the length of a brick in cm:"))
wall = float(input("Please enter the length of a wall in m:"))

## The brick and wall need to be in the same units.
wall = wall * 100

## 1cm is to be added to the brick length (to allow for concrete).
brick = brick + 1

## Calculate and display the bricks required.
numOfBricks = int(wall/brick)
print (numOfBricks,"bricks build one row of wall.")

##Calculate and display any remainder
wallRemainder = wall%brick
print ("This is",wallRemainder,"cm short of the required wall length")