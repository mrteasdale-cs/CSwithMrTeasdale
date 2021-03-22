# Puzzle Program 102
places = ["Glasgow","Swansea","Lisburn","Thurso","Bolton"]
letterCount = [0]*5
for loop in range(5):
	letterCount[loop] = places[loop].count("o")
print(places)
print(letterCount)