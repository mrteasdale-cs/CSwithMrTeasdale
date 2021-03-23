# Section 7 – File Handling
# Example 60 – Appending a Text File

hairColour = ["brown","red","white","black","blonde"]

with open('eyes.txt','a') as hairColourFile:
	for each in hairColour:
		hairColourFile.write(each+"\n")
