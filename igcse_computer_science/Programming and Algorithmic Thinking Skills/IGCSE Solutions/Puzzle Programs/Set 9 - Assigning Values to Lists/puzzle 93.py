# Puzzle Program 93
import math
numbers = [5]*5
numbers[3] = math.ceil(numbers[1]*3/2) - 3
numbers[0] = pow(numbers[3],2) - 16
numbers[4] = int(numbers[0]/4)
print(numbers)