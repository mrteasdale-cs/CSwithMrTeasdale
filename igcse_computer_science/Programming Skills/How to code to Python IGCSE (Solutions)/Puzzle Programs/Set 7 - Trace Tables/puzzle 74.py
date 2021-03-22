# Puzzle Program 74
num1 = 2
num2 = 4
for loop in range(4):
    num1 = num2 + num1
    num2 = num1 - loop
print(num1, num2)
