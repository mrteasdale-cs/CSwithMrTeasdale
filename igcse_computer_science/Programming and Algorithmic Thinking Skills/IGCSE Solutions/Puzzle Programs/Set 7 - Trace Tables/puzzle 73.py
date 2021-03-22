# Puzzle Program 73
num1 = 5
num2 = 5
num3 = 5
for loop in range(200):
	num3 = num1 - (num2 + 2)
	num2 = (num2 - 2) - num3
	num3 = num3 + 7
print(num1, num2, num3)