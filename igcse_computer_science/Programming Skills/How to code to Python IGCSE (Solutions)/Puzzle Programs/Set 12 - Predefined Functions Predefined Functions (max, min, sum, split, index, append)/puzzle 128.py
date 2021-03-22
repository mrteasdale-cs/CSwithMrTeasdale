# Puzzle Program 128
pageLength = "123 949 823 546 1002 398"
eachBookLength = pageLength.split(" ")
for loop in range(len(eachBookLength)):
	eachBookLength[loop] = int(eachBookLength[loop])
longestBook = max(eachBookLength)
print("The longest book =",longestBook,"pages.")