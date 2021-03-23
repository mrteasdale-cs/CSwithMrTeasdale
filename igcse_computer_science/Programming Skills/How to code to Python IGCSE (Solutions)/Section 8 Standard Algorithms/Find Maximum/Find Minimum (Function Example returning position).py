# Standard Algorithm
# Find Maximum (Function Example returning position)

def findMinPosition(minlist):
    minimum = minlist[0]
    position = 0
    for counter in range(1,len(minlist)):
        if minlist[counter] < minimum:
            minimum = minlist[counter]
            position = counter
    return position

names = ["Agattha","Elsebe","Ranneigh","Kolka","Magga"]
ages = [22,33,51,49,18]
print("Youngest person is:",names[findMinPosition(ages)])