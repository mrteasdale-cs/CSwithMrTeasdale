## Cinema Statistics
## Program 71
## With comments

## This is a good example of reusing code as this exact function,
## to read data from a text file, was used in program 68.
def readFileInto2DList(fileName):
    lines = []
    eachRow = []
    fileName = fileName + ".csv"
    with open(fileName,'r') as everything:
        for each in everything.readlines():
            row = each[0:-1]
            eachRow = row.split(",")
            lines.append(eachRow)
    return lines


## This procedure uses version 3 of the find Maximum standard algorithm
## to find the index of the maximum value in the 2D list.
## Note that all the data read from the file is still stored as text.
## To find the max screens we must change the data to a number using
## int() whenever we refer to the cinemaList[?][2] elements in each
## row of the 2D list.
def findMostScreens(cinemaList):
    maximum = int(cinemaList[0][2])
    position = 0
    for lines in range(1,len(cinemaList)):
        if int(cinemaList[lines][2]) > maximum:
            maximum = int(cinemaList[lines][2])
            position = lines
    print("The company with the most screens is:",cinemaList[position][0])


## To find the highest percentage the same code as above can be used
## with two changes.
## 1. The second index of the 2D list is changed from [?][2] to [?][3]
## 2. This index stores decimal values so int() must be change to float()
def findHighestPercentage(cinemaList):
    maximum = float(cinemaList[0][3])
    position = 0
    for lines in range(1,len(cinemaList)):
        if float(cinemaList[lines][3]) > maximum:
            maximum = float(cinemaList[lines][3])
            position = lines
    print("The company with highest percentage of total screens:",cinemaList[position][0])

## This procedure calculates the average screens by dividing the number
## of screens by the number of buildings.  Each average is then displayed
## with the cinema's name.
def findAverageScreens(cinemaList):
    print("The average number of screens each company has per building is:")
    for lines in range(0,len(cinemaList)):
        average = int(cinemaList[lines][2])/int(cinemaList[lines][1])
        print(cinemaList[lines][0],round(average,2))


## MAIN PROGRAM
allCinemas = []

file = "cinemas"
allCinemas = readFileInto2DList(file)
findMostScreens(allCinemas)
findHighestPercentage(allCinemas)
findAverageScreens(allCinemas)

## Extension Task
## The two find maximum procedures use more or less the same code.
## Rewrite the program so that a single function can be called twice
## to produce each of the outputs for max screens and max percentage.


