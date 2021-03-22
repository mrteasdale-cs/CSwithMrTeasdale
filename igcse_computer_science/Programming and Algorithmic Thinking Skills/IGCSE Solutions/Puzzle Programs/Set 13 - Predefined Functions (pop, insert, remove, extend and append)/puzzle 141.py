# Puzzle Program 141
points = [3,4,5,1,3,1,4]
above = []
average = sum(points)/len(points)
for loop in range(len(points)):
    if points[loop] > average:
        above.append(points[loop])
print(above)