# Puzzle Program 140
light = [5,1,3,1,4]
for loop in range(3):
    if light[loop] > 1:
        light.remove(light[loop])
print(light)