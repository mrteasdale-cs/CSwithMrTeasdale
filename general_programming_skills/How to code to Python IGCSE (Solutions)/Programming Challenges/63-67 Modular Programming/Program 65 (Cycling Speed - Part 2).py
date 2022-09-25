## Cycling Speed (Part 2)
## Program 65
## with comments

## This function is passed the list of revolutions, entered in the main
## program, and the circumference of the wheel.
def calcDistance(revolutions,circumference):
    ## The calculation for distance remains the same apart from the sum of
    ## the multiple revolutions must be calculated.
    distance = (circumference*sum(revolutions))/1000/1000
    return distance

## This function is passed the list of journey times, entered in the main
## program, and the distance calculated by function 1.
def calcAverageSpeed(distance,minutes):
    ## The calculation for time remains the same apart from the sum of
    ## the multiple minutes must be calculated.
    time = sum(minutes)/60
    speed = distance/time
    return speed

## Main Program
revolutions = []
minutes = []

circumference = int(input("What is the circumference of the wheel in millimetres."))

## Input each journey and add the information to the two lists.
journeys = int(input("How many journeys do you wish to enter?"))
for loop in range(journeys):
    print("Journey",loop+1)
    revs = int(input("How many wheel revolutions have taken place in your journey?"))
    revolutions.append(revs)
    mins = int(input("How many minutes did you cycle for?"))
    minutes.append(mins)

## Call the two functions.
distance = calcDistance(revolutions,circumference)
speed = calcAverageSpeed(distance,minutes)

## The results can then be displayed as before.
print ("You covered",round(distance,2),"km.")
print ("At an average speed of",round(speed,2),"kmph.")