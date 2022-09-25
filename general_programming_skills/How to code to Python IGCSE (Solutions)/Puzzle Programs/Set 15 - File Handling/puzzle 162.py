# Puzzle Program 162
scores = []
name = str(input("Please enter a name"))

with open('RCaverages.csv','r') as allScores:
    for each in allScores.readlines():
        each = each[0:-1]
        temp = each.split(",")
        if temp[0] == name:
            scores.append(temp[1])

print("The scores for",name,"were:")
for loop in range(len(scores)):
    print(scores[loop])
