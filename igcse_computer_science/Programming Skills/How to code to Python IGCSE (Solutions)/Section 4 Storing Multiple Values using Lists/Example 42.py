# Section 4 – Storing Multiple Values using Lists
# Example 42 – Outputting a list of lists (2D List structure) in rows and columns

temperature = [[0.0] * 24 for main in range(7)]
for day in range(7):
	for hour in range(24):
		temperature[day][hour]=float(input("Enter the next temperature"))

for day in range(7):
	for hour in range(24):
		print(temperature[day][hour],"",end=' ')
	print()

# If demonstrating this I would advise changing the ranges to smaller
# numbers rather than typing in 7*24 values.