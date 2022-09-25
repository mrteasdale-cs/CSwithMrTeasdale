# Puzzle Program 94
numbers = [10]*5
numbers[2] = numbers[1] + 15
numbers[3] = numbers[0]  - 5

if numbers[2] + numbers[4]  >= 35:
    numbers[0] = numbers[0] + 10
else:
	numbers[0] = numbers[0] - 10

if numbers[0]%2 == 1:
	numbers[4] = numbers[3] +2
else:
	numbers[4] = numbers[0] + 10

print(numbers)