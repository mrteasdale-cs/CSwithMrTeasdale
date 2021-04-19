import math

def radians_to_degrees():
    x = float(input("enter radians "))
    x = (180/math.pi) * x
    print("Degrees: ", x)

print(radians_to_degrees())
