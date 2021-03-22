# Puzzle Program 129
allTemperatures = "12,11,10,4,-2,5,8,20,23,24"
temperatures = allTemperatures.split(",")
for loop in range(len(temperatures)):
	temperatures[loop] = int(temperatures[loop])
print("The lowest temp =",min(temperatures))
print("The higest temp =",max(temperatures))