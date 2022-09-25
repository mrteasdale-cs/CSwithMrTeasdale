## Yearly Temperatures (Part 2)
## Program 72
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

## This procedure creates a separate list which stores only the temperatures
## of the day entered by the user.
def displayMinMaxTemp(allTemperatures,day):
    temp = []
    dayTemps = []
    for each in allTemperatures:
        ## Split each week in turn into separate strings.
        temp = each.split(",")
        ## Append one of the values in the above list, according to
        ## which day was entered, to the new list.
        dayTemps.append(int(temp[day]))

    ## After the above has been completed, a simple print can display
    ## the minimum and maximum values in the list.
    print("The min and max temperatures in day",day,"were",min(dayTemps),"and",max(dayTemps))

## The function compares each of the temperatures in the file data to
## a temperature entered by the user.  It returns the number of times
## the temperature is found.
def countTemperatures(allWeeks,temperature):
    temp = []
    total = 0
    for each in allWeeks:
        ## Split each week in turn into separate strings.
        temp = each.split(",")
        for tempIndex in range(1,8):
            ## Loop through each temperatures (except the first index as
            ## thats the week number) and compare it to the temperature
            ## the user entered.  If they match add one to the total.
            if int(temp[tempIndex]) == temperature:
                total += 1
    return total


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

## Ask for a valid day of the week and call the next procedure.
dayOfWeek = int(input("Please enter a day of the week"))
while dayOfWeek > 7 or dayOfWeek < 1:
    dayOfWeek = int(input("Please reenter a valid day from 1 to 7"))
displayMinMaxTemp(weeks,dayOfWeek)

## Ask for a temperature and then call a function to find and return
## the number of times that temperature is found in the file data.
singleTemp = int(input("Please enter a temperature"))
noOfOccasions = countTemperatures(weeks,singleTemp)
print("There were",noOfOccasions,"occasions that the temperature was",singleTemp,"degrees.")