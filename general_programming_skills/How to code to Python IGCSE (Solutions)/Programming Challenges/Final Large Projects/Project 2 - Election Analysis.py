## Election Analysis
## Project 2
## With comments

## The procedure below reads the data from the election file and
## returns a 2D list.
def readFromCSVFile():
    data = []

    with open('GE2017.csv','r') as everything:
        for each in everything.readlines():
            temp = each[0:-1]
            ## Each row of the file is split creating a sub-list which
            ## is then appended onto the data list.  Appending sub-lists
            ## in this way creates a 2D structure.
            tempList = temp.split(",")
            data.append(tempList)

    ## The heading (first) row in the file is removed from the data.
    data.pop(0)

    ## Each sublist stores 7 strings. The last five of these (elements
    ## 2 to 6 are converted to integers.  **Note 1 below
    for outer in range(len(data)):
        for inner in range(2,7):
            data[outer][inner] = int(data[outer][inner])
    return data

## This procedure compares the votes in the last two elements of the
## sub-lists to determine if one party got 15000 more votes than the
## other.  **Note 2 below
def safeSeats(geData,message,col1,col2):
    print(message)
    for constituency in range(len(geData)):
        ## The two sub-list elements, identified by the parameters col1 and
        ## col2, are compared to see to one is more than 15000 greater than the other.
        if geData[constituency][col1] > geData[constituency][col2] + 15000:
            ## Note 3 below
            filler = " " * (45-len(geData[constituency][0]))
            print(geData[constituency][0],filler,geData[constituency][1])

## This procedure compares the votes in each consistency.  If the difference is
## less than 1000 the difference and the consistuency name is appended to two lists.
def closeSeats(geData):
    constituencyName = []
    constituencyDifference = []

    for constituency in range(len(geData)):
        difference = geData[constituency][5] - geData[constituency][6]
        ## If sub-list element 6 is greater than 5 then the difference will be a
        ## negative number.  To ensure the difference is always stored as a positive
        ## value any negative answers are multiplied by -1.
        if difference < 0:
            difference = difference * -1
        if difference < 1000 and (geData[constituency][5]!=0 and geData[constituency][6]!=0):
            constituencyName.append(geData[constituency][0])
            constituencyDifference.append(difference)

    ## Bubble Sort of names and vote differences.
    ## This standard alogirithm uses the vote differences in the sort but to ensure
    ## that the names stay aligned with the differences both list elements must be sorted.
    for outerLoop in range(0,len(constituencyDifference)-1):
        for innerLoop in range(0,len(constituencyName)-(1+outerLoop)):
            if constituencyDifference[innerLoop] > constituencyDifference[innerLoop+1]:
                ## Swap the differences if in the wrong order.
                temp = constituencyDifference[innerLoop]
                constituencyDifference[innerLoop] = constituencyDifference[innerLoop+1]
                constituencyDifference[innerLoop+1] = temp
                ## Swap the names if the differences are in the wrong order.
                temp2 = constituencyName[innerLoop]
                constituencyName[innerLoop] = constituencyName[innerLoop+1]
                constituencyName[innerLoop+1] = temp2

    for constituency in range(len(constituencyName)):
        print(constituencyName[constituency],constituencyDifference[constituency])

## This function is the count occurences standard algorithm.
def spoiltBallots(geData):
    total = 0
    for constituency in range(len(geData)):
        ## Every times the invalid votes value in the sub-list is greater than
        ## 200, 1 is added to the total.
        if geData[constituency][4] > 200:
            total += 1
    return total


## MAIN PROGRAM

## A function is called to read the data from a file and return a
## 2D list.
electionData = []
electionData = readFromCSVFile()

## The same procedure is called twice with different parameters.
heading = "Conservative seats safe from Labour"
safeSeats(electionData,heading,5,6)

heading = "Labour seats safe from Conservative"
safeSeats(electionData,heading,6,5)

## A procedure is called to determine and display places where the
## difference in the votes was less than 1000.
closeSeats(electionData)

## Call a function which returns the number of places where more than
## 200 people spoilt their voting paper.
print("The number of constituences with more than 200 invalid votes was")
print(spoiltBallots(electionData))

## **Note 1 - The conversion of strings to integers in the data is done
## at this point rather than later on in the other modules.
## One conversion now rather than repeating  several conversions later
## is more efficient.

## **Note 2 - This could have been written as two seprate procedures.  One
## for Conservative and one for Labour.  This example shows how using parameters
## (to store the changing message and the order the different elements that
## will be compared) can reduce two procedures to one.

## **Note 3 - This was just added as a bit of fun to show how spaces can be added
## between the two dispayed values. By calculating the correct number
## of spaces to add two precise columns can be displayed. This is a work around
## designed to only use code from the book.  If you wish to learn how to do this
## properly search the web for "Python 3 formatted output".