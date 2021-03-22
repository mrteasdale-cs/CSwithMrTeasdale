# Section 4 – Storing Multiple Values using Lists
# Example 41 - Adding user input to a list of lists (2D List structure)
# Nested Loop for larger sub-list

temperature = [[0.0] * 24 for main in range(7)]
for day in range(7):
	for hour in range(24):
		temperature[day][hour]=float(input("Enter the next temperature"))
