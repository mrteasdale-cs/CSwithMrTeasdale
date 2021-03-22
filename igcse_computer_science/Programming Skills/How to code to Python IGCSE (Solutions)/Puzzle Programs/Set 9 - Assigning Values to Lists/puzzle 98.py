# Puzzle Program 98
numbers = [2]*5
for loop in range(4):
	numbers[loop+1] = numbers[loop] + loop+1
print(numbers)