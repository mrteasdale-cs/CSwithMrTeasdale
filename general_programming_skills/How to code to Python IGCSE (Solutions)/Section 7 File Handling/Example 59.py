# Section 7 – File Handling
# Example 59 – Writing to a Text File

eyeColour = ["blue","brown","green"]

with open('eyes.txt','w') as eyeColourFile:
	for each in eyeColour:
		eyeColourFile.write(each + "\n")