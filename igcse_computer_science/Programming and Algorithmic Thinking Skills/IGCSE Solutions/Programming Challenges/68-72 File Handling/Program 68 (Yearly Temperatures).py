## Yearly Temperatures
## Program 68
## With comments

## Note that this module has been written so that it does not use
## variable and list names associated with the task.  Writing this
## way allows you to reuse code for other programs.
def readFromTextFile(fileName):
    lines = []
    fileName = fileName + ".txt"
    with open(fileName,'r') as everything:
        for each in everything.readlines():
            lines.append(each[0:-1])
    return lines

## The module to calcualate the average temperature over weeks is
## quite specific to the task so uses appropraite variable names.
def calculateAverage(temperatures,start,end):
    temp = []
    total = 0

    for eachWeek in range(start-1,end):
        ## The list 'temperatures' that was passed into this procedure
        ## currently stores an entire week in each element.
        ## Start by spliting a week into a temporary list of elements.
        temp = temperatures[eachWeek].split(",")

        ## Remove the first element as its the week number and not required.
        temp.pop(0)

        ## Add up the remaining temperature values in the temporary list.
        for loop in range(7):
            total = total + int(temp[loop])

    ## Divide total by the number of days (weeks * 7).
    average = total / ((end+1-start)*7)
    print("The average temperature for weeks",start,"to",end)
    print(round(average,2),"degrees")

## MAIN PROGRAM
weeks = []

file = "yearTemperatures"
weeks = readFromTextFile(file)

## Get valid start and final week numbers.
first = int(input("Please enter the starting week"))
while first < 1:
    first = int(input("Please reenter a valid starting week"))

## Note that the validation ensures the second week is greater than
## the first.
second = int(input("Please enter the final week"))
while second > 52 or second < first:
    second = int(input("Please reenter a valid final week"))

calculateAverage(weeks,first,second)

## Note - Included in the folder is a program I wrote to create the
## random temperature data.  Run this again to create a new data set.

## Extension Task
## Write the same program using a 2D list.  The file data should be read
## and stored directly into the 2D list. Store only the weeks you require
## hint - the week numbers are in the file data.
## The 2D list should traversed as before to calculate the average.