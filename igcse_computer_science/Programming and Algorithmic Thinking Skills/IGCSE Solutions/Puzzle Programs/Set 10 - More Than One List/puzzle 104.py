# Puzzle Program 104
numbers = [45,9,35,92,67]
temporary = 0
for loop in range(4):
	if numbers[loop] > numbers[loop+1]:
		temporary = numbers[loop]
		numbers[loop] = numbers[loop+1]
		numbers[loop+1] = temporary
print(numbers)