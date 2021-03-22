# Puzzle Program 103
elements = ["Copper"," Titanium"," Iron"," Lead"," Silicon"]
for loop in range(5):
	if elements[loop].count("i") > 1:
		elements[loop] = elements[4-loop]
print(elements)