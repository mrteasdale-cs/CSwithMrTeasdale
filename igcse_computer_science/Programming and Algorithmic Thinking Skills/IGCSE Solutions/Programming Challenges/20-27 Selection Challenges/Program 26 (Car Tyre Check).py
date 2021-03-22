## Car Tyre Check
## Program 26
## With Comments

## The user is asked to input their speed and stopping distance:

speed = int(input("Please enter the test speed (mph)"))
distance = float(input("Please enter the tested stopping distance (m)"))

## The program now makes a decision about whether the car has passed.

if speed == 30 and distance <= 14:
    print ("Your car passed the test")
elif speed == 50 and distance <= 38:
    print ("Your car passed the test")
else:
    print("Your car failed the braking distance test.")

## The above if statement checks each speed in turn along with the
## stopping distance entered.
## If the distance is acceptable a pass message is displayed.
## If all the elifs and if are all found to be false the else is then true.
## This means the car must have failed the test.
## An appropriate fail message is displayed.