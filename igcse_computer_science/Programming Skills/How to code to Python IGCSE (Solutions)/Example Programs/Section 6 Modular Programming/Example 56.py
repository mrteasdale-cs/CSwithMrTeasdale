# Section 6 – Modular Programming
# Example 56 – Writing to Reuse Code

def displayData(dataInput,message):
	average = sum(dataInput)/len(dataInput)
	print("Average " + message.lower(),round(average,1))
	print(message + "s ranged from:")
	print(min(dataInput),"to", max(dataInput))
	print()

# Main Program
scores = [4,6,8,5,6,3,5,9,10,2,4,6,3,5]
title = "Score"
displayData(scores,title)

pHReadings = [3.4,3.7,3.0,4.2,5.0,2.7,3.2]
text = "pH"
displayData(pHReadings,text)

heights = [154,158,187,172,155,190,182]
word = "Height"
displayData(heights,word)