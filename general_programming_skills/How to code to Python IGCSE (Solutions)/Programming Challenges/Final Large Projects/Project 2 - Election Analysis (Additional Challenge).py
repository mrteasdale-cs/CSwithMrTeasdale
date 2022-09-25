## Election Analysis (Additional Challenge)
## Project 2
## With comments

def readFromCSVFile():
    data = []

    with open('GE2017.csv','r') as everything:
        for each in everything.readlines():
            temp = each[0:-1]
            tempList = temp.split(",")
            data.append(tempList)

    data.pop(0)

    for outer in range(len(data)):
        for inner in range(2,7):
            data[outer][inner] = int(data[outer][inner])
    return data


def safeSeats(geData,message,col1,col2):
    print(message)
    for constituency in range(len(geData)):

        if geData[constituency][col1] > geData[constituency][col2] + 15000:
            filler = " " * (45-len(geData[constituency][0]))
            print(geData[constituency][0],filler,geData[constituency][1])


def closeSeats(geData):
    constituencyName = []
    constituencyDifference = []

    for constituency in range(len(geData)):
        difference = geData[constituency][5] - geData[constituency][6]

        if difference < 0:
            difference = difference * -1
        if difference < 1000 and (geData[constituency][5]!=0 and geData[constituency][6]!=0):
            constituencyName.append(geData[constituency][0])
            constituencyDifference.append(difference)

    for outerLoop in range(0,len(constituencyDifference)-1):
        for innerLoop in range(0,len(constituencyName)-(1+outerLoop)):
            if constituencyDifference[innerLoop] > constituencyDifference[innerLoop+1]:

                temp = constituencyDifference[innerLoop]
                constituencyDifference[innerLoop] = constituencyDifference[innerLoop+1]
                constituencyDifference[innerLoop+1] = temp

                temp2 = constituencyName[innerLoop]
                constituencyName[innerLoop] = constituencyName[innerLoop+1]
                constituencyName[innerLoop+1] = temp2

    for constituency in range(len(constituencyName)):
        print(constituencyName[constituency],constituencyDifference[constituency])


def spoiltBallots(geData):
    total = 0
    for constituency in range(len(geData)):

        if geData[constituency][4] > 200:
            total += 1
    return total


## This procedure combines the votes for Conservative and Labour combined.  If this
## total is less than 50% of the total votes the name of the consitituency is displayed.
def displayLessThan50(geData):
    ## Create two empty lists to store the names and countries of identified consitituencies.
    tempNames = []
    tempCountry = []

    print("Consitituences where the combined Conservative + Labour vote was less than 50% of all votes.")
    for constituency in range(len(geData)):
        total = geData[constituency][5] + geData[constituency][6]
        if geData[constituency][3] * 0.5 > total:
            ## If a constituency is identified append its details to the new lists.
            tempNames.append(geData[constituency][0])
            tempCountry.append(geData[constituency][1])

    ## Bubble sort on tempCountry list (swapping tempNames at the same time).
    for outerLoop in range(0,len(tempNames)-1):
        for innerLoop in range(0,len(tempNames)-(1+outerLoop)):
            if tempCountry[innerLoop] > tempCountry[innerLoop+1]:

                temp = tempNames[innerLoop]
                tempNames[innerLoop] = tempNames[innerLoop+1]
                tempNames[innerLoop+1] = temp

                temp2 = tempCountry[innerLoop]
                tempCountry[innerLoop] = tempCountry[innerLoop+1]
                tempCountry[innerLoop+1] = temp2

    ## Display the sorted lists.
    for constituency in range(len(tempNames)):
        print(tempCountry[constituency],tempNames[constituency])


## MAIN PROGRAM

electionData = []
electionData = readFromCSVFile()

heading = "Conservative seats safe from Labour"
safeSeats(electionData,heading,5,6)

heading = "Labour seats safe from Conservative"
safeSeats(electionData,heading,6,5)

closeSeats(electionData)

print("The number of constituences with more than 200 invalid votes was")
print(spoiltBallots(electionData))

## Call a procedure to display consistuences where less than 50% of voters
## voted for Conservative and Labour combined.
displayLessThan50(electionData)


