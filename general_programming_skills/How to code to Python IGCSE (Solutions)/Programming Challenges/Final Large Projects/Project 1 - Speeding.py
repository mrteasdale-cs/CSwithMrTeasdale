## Speeding
## Project 1
## With comments

## The function below checks to see if the file exists and then read
## any data from the file into a list.  The list is returned to
## the main program.
def readPreviousFromFile():
    data = []

    ## First open an 'append' connection to the file.  This ensures that
    ## if the file doesn't exist the program will create a new file.
    ## Note that if a 'write' connection was opened the contents of the
    ## file would be deleted.
    with open('speeding.txt','a') as check:
        print("Checking File")

    ## Read in the previous data from the file. If the file is empty
    ## an empty list will be returned.
    with open('speeding.txt','r') as everything:
        for each in everything.readlines():
            data.append(each[0:-1])
    return data


## The functions below extract the age and speed, returning two separate
## lists of data.
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


## This procedure calculates the number of cars and the number of those
## cars that failed to keep within the speed limit.  These values can be
## used to calculate and display the percentage of cars that were speeding.
def displayPercentage(carResults):
    totalCars = len(carResults)
    totalFails = sum(carResults)
    percentage = 100 / totalCars * totalFails
    print("Speeding -",str(percentage)+"%")
    print("Not Speeding -",str(100-percentage)+"%")


## This function loops through the car data and uses a separate list to
## keep a total of the number of fails for each age of car.
## Note that as well as displaying the required output, the new list is
## returned as it is needed in the next procedure.
def displayFailsByAge(carAges,carResults):
    speedingByAge = [0]*120

    for loop in range(len(carAges)):
        ## If a car was caught speeding.
        if carResults[loop] == 1:
            ## The line below uses the age of each car as a list index.
            ## Note that as the ages start at 1 and list indexes start
            ## at 0 the ages are offset by -1 (1 year old cars are stored
            ## at index 0, 2 year old at 1 and so on).
            speedingByAge[carAges[loop]-1] += 1

    for loop in range(max(carAges)):
        ## Display the totals of speeding cars for each age.  Remembering
        ## to account for the offset (loop+1).
        print(loop+1,"-",speedingByAge[loop])

    return speedingByAge


## This procedure finds maximum value in the list of speeding totals and
## then finds the index of this value.  The index is then used to display
## the age of the car that was caught speeding the most (index+1).
def mostFrequentSpeeder(speedingByAge):
    worst = speedingByAge.index(max(speedingByAge)) + 1
    print(str(worst)+"-year-old cars were the worst speeding offenders.")


## The final procedure writes the complete car speeding data back to the
## file.  Note that as the saved data was read in, the file data should be
## completelly over-written with the old and new data.
def writeDataToFile(carAges,carResults):
    with open('speeding.txt','w') as carFile:
        for loop in range(len(carAges)):
            carFile.write(str(carAges[loop])+","+str(carResults[loop])+"\n")



## MAIN PROGRAM

## Get any previously stored data.
speedingData = []
speedingData = readPreviousFromFile()

## The next two functions extract the car ages and speeding results
## from the file data, storing the ages and speeding results in two parallel lists.
## ** See extra notes below **
ages = []
results = []
ages = extractAges(speedingData)
results = extractResults(speedingData)

## Get new data from user.
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

## Call a procedure to display the percentage of fails.
displayPercentage(results)

## Call a procedure to display the number of cars of each age that were
## caught speeding.
speedingTotals = []
speedingTotals = displayFailsByAge(ages,results)

## Using the list created above call a procedure to display the age of
## car that most often broke the speed limit.
mostFrequentSpeeder(speedingTotals)

## Finally pass the data to a procedure which will update the stored data.
writeDataToFile(ages,results)



## ** Extra Notes
## 1. The example answer has been written to show a solution with two
## separate lists storing the data.  It could just have easily been
## written using a 2D list.
## 2. Python functions can return and assign more than one value.  As
## examples of this have not been given in the book, two separate functions
## have been used to return the two lists one at a time.
