## Cycling Speed
## Program 19
## with comments

## The user should be asked to enter the bikes wheel circumference,
## number of wheel revolution and the number of minutes the journey
## lasted.

circumference = int(input("What is the circumference of the wheel in millimetre?"))
revolutions = int(input("How many wheel revolutions have taken place in your journey?"))
minutes = int(input("How many minutes did you cycle for?"))

## To calculate the speed, the distance and time must be calculated
## and converted to the correct units.

## There are 1000mm in a metre and 1000 metres in a kilometre.
distance = (circumference*revolutions)/1000/1000

## There are 60 minutes in 1 hour.
time = minutes/60

## Speed can then be calcuated.
speed = distance/time

## The results can then be displayed.
print ("You covered",distance,"km.")
print ("At an average speed of",speed,"kmph.")