# Puzzle Program 51
import math
num1 = 12.7
num2 = 30.3
num3 = (int(num2) - math.ceil(num1))
num4 = pow(3,(num3%5))
print (num4*(int(num2/10)))