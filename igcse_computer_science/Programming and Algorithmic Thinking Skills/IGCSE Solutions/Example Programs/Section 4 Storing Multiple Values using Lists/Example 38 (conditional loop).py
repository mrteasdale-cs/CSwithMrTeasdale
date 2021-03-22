# Section 4 – Storing Multiple Values using Lists
# Example 38 – Input into a list using fixed and conditional loops
# Conditional loop

names = [""]*0
ages = [0]*0
counter = 0
morePeople = "Y"
while morePeople.lower() == "y":
	names.append(str(input("Please enter name " + str(counter+1))))
	ages.append(int(input("Please enter " + names[counter] + "’s age")))
	morePeople  = str(input("Do you wish to enter more?  Y/N"))
	if morePeople.lower()  != "y":
		print("Entry complete")
	else:
		counter = counter + 1
