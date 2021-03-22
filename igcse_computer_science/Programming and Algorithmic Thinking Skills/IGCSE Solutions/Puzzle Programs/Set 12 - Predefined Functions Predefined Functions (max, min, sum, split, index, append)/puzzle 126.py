# Puzzle Program 126
cricketScores = "2,3,0,0,0,1-0,0,0,2,3,0-1,1,0,0,0,6"
overScores = cricketScores.split("-")
for loop in range(len(overScores)):
	oneOver = overScores[loop]
	print("The first ball =",oneOver[0:1])