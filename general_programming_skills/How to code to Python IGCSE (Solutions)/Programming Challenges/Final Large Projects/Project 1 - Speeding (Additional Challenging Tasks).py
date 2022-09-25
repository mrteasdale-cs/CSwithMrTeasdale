## Speeding (Additional Challenging Tasks)
## Project 1
## With comments

def readPreviousFromFile():
    data = []

    with open('speeding.txt','a') as check:
        print("Checking File")

    with open('speeding.txt','r') as everything:
        for each in everything.readlines():
            data.append(each[0:-1])
    return data


def extractAges(speedingData):
    carAges = []
    temp = []
    for each in speedingData:
        temp = each.split(",")
        carAges.append(int(temp[0]))
    return carAges

def extractResults(speedingData):
    carResults = []
    temp = []
    for each in speedingData:
        temp = each.split(",")
        carResults.append(int(temp[1]))
    return carResults


def displayPercentage(carResults):
    totalCars = len(carResults)
    totalFails = sum(carResults)
    percentage = 100 / totalCars * totalFails
    print("Speeding -",str(percentage)+"%")
    print("Not Speeding -",str(100-percentage)+"%")


def displayFailsByAge(carAges,carResults):
    speedingByAge = [0]*120

    for loop in range(len(carAges)):
        if carResults[loop] == 1:
            speedingByAge[carAges[loop]-1] += 1

    for loop in range(max(carAges)):
        print(loop+1,"-",speedingByAge[loop])

    return speedingByAge


def mostFrequentSpeeder(speedingByAge):
    worst = speedingByAge.index(max(speedingByAge)) + 1
    print(str(worst)+"-year-old cars were the worst speeding offenders.")


def writeDataToFile(carAges,carResults):
    with open('speeding.txt','w') as carFile:
        for loop in range(len(carAges)):
            carFile.write(str(carAges[loop])+","+str(carResults[loop])+"\n")


## This procedure is passed the ages and results lists.  It uses this data to
## work out the percentage of old and new speeding cars.  The user can input
## where the cutoff age is for a car being regarded as old or new.
def displayOldvsNew(carAges,carResults):
    ## This procedure is going to split the current lists up into two so
    ## four new lists are required.
    oldAges = []
    oldResults = []
    newAges = []
    newResults = []

    cutOff = int(input("Please enter the cutoff age for old cars."))

    for loop in range(len(carAges)):
        ## If the car at the beginning of the passed list has an age greater
        ## then or equal to the cut off age, remove the first item from the
        ## Age and Result lists. Append the removed items to the list for 'old' cars.
        if carAges[0] >= cutOff:
            oldAges.append(carAges.pop(0))
            oldResults.append(carResults.pop(0))
        ## If the car is newer, do the same as the above but add the two removed
        ## items to the 'new' lists.
        else:
            newAges.append(carAges.pop(0))
            newResults.append(carResults.pop(0))

    ## Calculate the percentage of speeding cars for old and new lists.
    ## Display results according to which were the worst speeders.
    percentageNew = 100/len(newAges)*sum(newResults)
    percentageOld = 100/len(oldAges)*sum(oldResults)
    print("The percentage of new cars speeding is:",round(percentageNew,1))
    print("The percentage of old cars speeding is:",round(percentageOld,1))
    if percentageNew > percentageOld:
        print("New cars were the worst speeding offenders.")
    elif percentageOld > percentageNew:
        print("Old cars were the worst speeding offenders.")
    else:
        print("Both old and new cars were caught speeding equally as often.")



## MAIN PROGRAM

speedingData = []
speedingData = readPreviousFromFile()

ages = []
results = []
ages = extractAges(speedingData)
results = extractResults(speedingData)

newAge = 0
while newAge != 999:
    newAge = int(input("Please enter the age of the new car."))
    if newAge != 999:
        while newAge < 1 or newAge > 120:
            newAge = int(input("Please reenter a valid age from 1 to 120."))
        ages.append(newAge)

        speedResult = int(input("Please enter the speeding result"))
        while speedResult < 0 or speedResult > 1:
            speedResult = int(input("Please reenter a valid speeding result 1 or 0."))
        results.append(speedResult)

displayPercentage(results)

speedingTotals = []
speedingTotals = displayFailsByAge(ages,results)

mostFrequentSpeeder(speedingTotals)

writeDataToFile(ages,results)

## Call the new procedure.
displayOldvsNew(ages,results)


