# Puzzle Program 142
one = [3,4,5,1,5,1,4,3]
two = []
three = []
for loop in range(len(one)-1,-1,-1):
    two.append(one[loop])
print(two)
for loop in range(len(one)):
    if one[loop]==two[loop]:
        three.append(1)
    else:
        three.append(0)
print(three)