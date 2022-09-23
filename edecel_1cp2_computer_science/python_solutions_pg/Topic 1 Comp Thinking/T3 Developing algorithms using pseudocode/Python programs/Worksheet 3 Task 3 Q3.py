totalScore = 0
numScore = 0
score = 0
while score != -1:
    print("Please enter the next score, -1 to end: ")
    score = int(input())
    if score != -1:
        numScore = numScore + 1
        totalScore = totalScore + score
average = totalScore / numScore
print(average)

#To allow for the user entering -1 before entering any scores, the last two statements could be altered to:
if numScore == 0:
    print("Program ended")
else:
    average = totalScore / numScore
print(average)

