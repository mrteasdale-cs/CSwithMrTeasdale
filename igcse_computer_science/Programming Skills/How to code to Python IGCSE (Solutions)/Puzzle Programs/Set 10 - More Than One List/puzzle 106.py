# Puzzle Program 106
values = [45.78, 12.34, 102.14, 5.26, 1034.99]
temp1 = 0
for num in range(5):
	temp1 = values[num] - int(values[num])
	values[num] = int(temp1*10)
print(values)