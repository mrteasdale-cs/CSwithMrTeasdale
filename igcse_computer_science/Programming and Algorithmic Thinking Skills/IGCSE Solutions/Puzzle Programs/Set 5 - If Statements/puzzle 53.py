# Puzzle Program 53
temp = int(input("Please enter a temperature"))
if temp >= -273 and temp <= 42:
	print("Solid")
elif temp >43 and temp < 87:
	print("Liquid")
else:
	print("Gas")
