## Archery Scores
## Project 3
## With comments

import random

## A function to combine the contents of a list with new content read from a file.
def readFromTextFile(fileName,filelines):
    ## Open the passed file name and append each new line to the passed list.
    fileName = fileName + ".txt"
    with open(fileName,'r') as everything:
        for each in everything.readlines():
            filelines.append(each[0:-1])
    ## The list with the previous and new file information is returned.
    return filelines

## A function that splits each line of the passed file, using a single space
## character, to identify where to split the data.
def create2DList(filelines):
    singleLine = []
    temp = []
    for each in filelines:
        singleLine = each.split(" ")
        ## The last element of the split data (the score) is converted to an integer.
        singleLine[2] = int(singleLine[2])
        ## The split list is copied back over the original single string.
        temp.append(singleLine)
    return temp

## A function that sorts the 2D list using the 'score' element of each sub-list.
## The function uses the 'Insertion Sort' standard algorithm.
def insertionSort(values):
    for index in range(1,len(values)):
        currentscore = values[index]
        position = index
        ## A second index [2] has to be added to the standard algorithm to
        ## identify where one score was less than another.
        while position>0 and values[position-1][2]<currentscore[2]:
            values[position]=values[position-1]
            position = position-1
        values[position]=currentscore
    return values

## A function that identifies 35 archers from the sorted list.
def identify35(archers):

    ## The top 30 scores are removed from the list and added to a new list.
    top35 = []
    for loop in range(30):
        top35.append(archers.pop(0))

    ## Remove any archers who didn't score 650 or more.
    found = "yes"
    while found == "yes":
        if archers[len(archers)-1][2] < 650:
            archers.pop()
        else:
            found = "no"

    ## Using the remaining archers (not top 30 but scored over 650), randomly
    ## select an element from the list, remove it using pop() and add it to
    ## the list of top 30 archers.
    for loop in range(5):
        top35.append(archers.pop(random.randint(0,len(archers)-1)))

    return top35

## A function which uses the insertion sort code from before.
def insertionSortSurname(values):
    for index in range(1,len(values)):
        currentscore = values[index]
        position = index
        ## This time index [1] of the sub-list, 'surname', was used to
        ## sort the list.
        while position>0 and values[position-1][1]>currentscore[1]:
            values[position]=values[position-1]
            position = position-1
        values[position]=currentscore
    return values

## A simple procedure that displays the final, sorted list of 35 archers.
def displaySelectedArchers(finalList):
    print("List of selected world archers:")
    for each in finalList:
        print(each[0],each[1],each[2])



## MAIN PROGRAM

archeryScores = []

## Call the readFromTextFile function three times.  Each call passes
## the archeryScores list and a file name.  The list is returned each time
## with the extra information added from the selected file.
file = "americas"
archeryScores = readFromTextFile(file,archeryScores)
file = "asia"
archeryScores = readFromTextFile(file,archeryScores)
file = "europe"
archeryScores = readFromTextFile(file,archeryScores)

## Call a function that splits each line on the archeryScores list into a
## sub-list, creating a 2D list.
archeryScores2D = create2DList(archeryScores)

## Call a sort function to re-order the 2D list and return the sorted list.
archeryScores2D = insertionSort(archeryScores2D)

## Call a function that identifies the names of 35 archers according to the
## requirements.
competitionList = identify35(archeryScores2D)

## Call a function to sort the identified list of archers, this time by surname.
competitionList = insertionSortSurname(competitionList)

## Display the final list of sorted archers names and scores.
displaySelectedArchers(competitionList)