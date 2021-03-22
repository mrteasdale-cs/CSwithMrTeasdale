## Average Temperature
## Program 32
## With Comments

## A total variable is set to 0.  This will be used later.
## An initial message is displayed:

total = 0
print("Please enter the seven temperatures.")

## In this challenge an input is placed inside a loop.
## The loop repeats the following 7 times
##   - the user is asked for an input (temperature)
##   - each input is added onto the total.

for loop in range(7):
    temperature = int(input())
    total = total + temperature

## The total is divided by 7 to get the average.
## A message with the final average is displayed.

average = total/7
print("This week’s average was:")
print(round(average,2),"degrees centigrade")