## Average Temperature - Part 2
## Program 44
## With Comments

## A fixed loop is added so that the original code repeats 4 times using
## the range(1,5)
for weeks in range(1,5):
    ## The loop variable 'weeks' is used to display a diffferent numbered
    ## week each repetition.
    print("Week",weeks)

    ## The previous code is indented (moved right) so that it is inside the loop.
    total = 0
    print("Please enter the seven temperatures.")

    for loop in range(7):
        temperature = int(input())

        while not(temperature >= -40 and temperature <= 55):
            print("Temperature should be between -40 and 55")
            temperature = int(input())

        total = total + temperature

    average = total/7

    ## The loop variable is used again in the output to ensure the correct
    ## week number is displayed each repetition.
    print("Week",weeks,"average was:")

    print(round(average,2),"degrees centigrade")