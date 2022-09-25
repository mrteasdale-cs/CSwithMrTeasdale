# Puzzle Program 75
num1 = 4
num2 = 6
num3 = 0
for loop in range(3,7):
    num1 = (num1/2 + num2/3) * loop
    num3 = num2 + num1
print(int(num1), num2, int(num3))