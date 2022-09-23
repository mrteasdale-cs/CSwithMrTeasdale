totalScore = 0
numScore = 0
moreScores = True
while moreScores:
    score = int(input("Enter the next score, -1 to end: "))
    if score != -1:
        numScore = numScore + 1
        totalScore = totalScore + score
    else:
        moreScores = False

#allow for user entering no scores

if numScore == 0:
    print("\nNo scores entered - program ended")
else:
    averageScore = totalScore/numScore
    print("Average score: ", averageScore)
