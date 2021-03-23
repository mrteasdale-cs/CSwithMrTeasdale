# Section 4 – Storing Multiple Values using Lists
# Example 41 - Adding user input to a list of lists (2D List structure)

members = [[""] * 2 for main in range(3)]

for people in range(3):
	members[people][0]=str(input("Please enter the forename of person, people"))
	members[people][1]=str(input("Please enter the surname of person, people"))

for people in range(3):
	print(members[people][0],members[people][1])