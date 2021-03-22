## Archery Scores (Additional Challenge)
## Project 3
## With comments

import random

def readFromTextFile(fileName,filelines):
    fileName = fileName + ".txt"
    with open(fileName,'r') as everything:
        for each in everything.readlines():
            filelines.append(each[0:-1])
    return filelines

def create2DList(filelines):
    singleLine = []
    temp = []
    for each in filelines:
        singleLine = each.split(" ")

        singleLine[2] = int(singleLine[2])

        temp.append(singleLine)
    return temp

def insertionSort(values):
    for index in range(1,len(values)):
        currentscore = values[index]
        position = index
        while position>0 and values[position-1][2]<currentscore[2]:
            values[position]=values[position-1]
            position = position-1
        values[position]=currentscore
    return values

def identify35(archers):
    top35 = []
    for loop in range(30):
        top35.append(archers.pop(0))
    found = "yes"
    while found == "yes":
        if archers[len(archers)-1][2] < 650:
            archers.pop()
        else:
            found = "no"
    for loop in range(5):
        top35.append(archers.pop(random.randint(0,len(archers)-1)))
    return top35

def insertionSortSurname(values):
    for index in range(1,len(values)):
        currentscore = values[index]
        position = index
        while position>0 and values[position-1][1]>currentscore[1]:
            values[position]=values[position-1]
            position = position-1
        values[position]=currentscore
    return values

def displaySelectedArchers(finalList):
    print("List of selected world archers:")
    for each in finalList:
        print(each[0],each[1],each[2])


## An additional function is added to merge the two lists. The function takes
## each USA competitor in turn and checks if they are already in the archeryScores2D
## list.
## If they are -  the score is compared and the archeryScores2D is updated, if required
##                with the larger of the competitor's two scores.
## If they are not - the whole of the competitor's details are appended onto the
##                   archeryScores2D list as they are a new archer.
def mergeFiles(usaArchers,archeryScores2D):
    while len(usaArchers) > 0:
        ## Remove (using the pop() pre-defined function) and store one of the USA archers.
        archer = usaArchers.pop()
        ## Call the 'Linear Search' function below to find and return the list index of
        ## the selected archer in the archeryScores2D list.
        position = checkNames(archer,archeryScores2D)
        if position == -1:
            archeryScores2D.append(archer)
        else:
            if archeryScores2D[position][2] < archer[2]:
                archeryScores2D[position][2] = archer[2]
    return archeryScores2D

## Check to see if the archer exists in the archeryScores2D list.
## If they do return their position in the list, if they do not return -1.
def checkNames(target,archeryScores2D):
    index = -1
    for names in range(len(archeryScores2D)):
        if archeryScores2D[names][0] == target[0] and archeryScores2D[names][1] == target[1]:
            index = names
    return index



## MAIN PROGRAM

archeryScores = []

file = "americas"
archeryScores = readFromTextFile(file,archeryScores)
file = "asia"
archeryScores = readFromTextFile(file,archeryScores)
file = "europe"
archeryScores = readFromTextFile(file,archeryScores)

archeryScores2D = create2DList(archeryScores)

## Additional Task
## The first part of the additional task reuses two of the functions
## already created.

## Create a separate list for the USA results and read the data from
## the file into the list.
usaArchers = []
file = "USA"
archeryScores = readFromTextFile(file,usaArchers)

## Call the function that converts the 1D list to a 2D list.
usaArchers2D = create2DList(usaArchers)


## Now call a new function to merge the two files according to the
## requirements.
archeryScores2D = mergeFiles(usaArchers2D,archeryScores2D)


## The program can now continue as before to select, sort and display
## 35 archers.
archeryScores2D = insertionSort(archeryScores2D)
competitionList = identify35(archeryScores2D)
competitionList = insertionSortSurname(competitionList)
displaySelectedArchers(competitionList)