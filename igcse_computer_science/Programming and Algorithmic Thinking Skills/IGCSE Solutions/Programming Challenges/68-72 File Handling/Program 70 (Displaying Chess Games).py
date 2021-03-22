## Displaying Chess Games
## Program 70
## With comments

## This is a good example of reusing code as this exact function,
## to read data from a text file, was used in program 68.
def readFromTextFile(fileName):
    lines = []
    fileName = fileName + ".txt"
    with open(fileName,'r') as everything:
        for each in everything.readlines():
            lines.append(each[0:-1])
    return lines


## This function replaces the game codes (- x +) with appropraite text.
def formatLine(gameList):
    for lines in range(len(gameList)):
        gameList[lines] = gameList[lines].replace("-"," to ")
        gameList[lines] = gameList[lines].replace("x"," takes ")
        gameList[lines] = gameList[lines].replace("+"," check")
    return gameList


## The final procedure simply dispays each line with "Move" concatenated
## at the beginning of the line.
def displayGame(gameList):
    for each in gameList:
        print("Move",each)


## MAIN PROGRAM
game = []

file = "chessGame"
game = readFromTextFile(file)
game = formatLine(game)
displayGame(game)