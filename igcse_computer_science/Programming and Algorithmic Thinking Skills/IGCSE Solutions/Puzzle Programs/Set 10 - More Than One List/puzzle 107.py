# Puzzle Program 107
import math
firstValue = [7.7, 3.2, 5.2, 6.4, 8.9]
secondValue = [9, 6, 4, 12, 10]
for num in range(5):
	if round(firstValue[num]) > firstValue[num]:
		secondValue[num] = secondValue[num] * math.ceil(firstValue[num])
	else:
		secondValue[num] = secondValue[num] * math.ceil(firstValue[num]) / 2
	if secondValue[num] > 50:
		firstValue[num] = 99
	else:
		firstValue[num] = 0
print(firstValue)
print(secondValue)