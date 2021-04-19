import math

def radians_to_degrees():
    try:
        x = float(input("enter radians "))

        if x.isnumeric():
            x = (180/math.pi) * x
            print("Degrees: ", x)
        else:
            print("Not a float!")
    except:
        print("Not a number!")

print(radians_to_degrees())
