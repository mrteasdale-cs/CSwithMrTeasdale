# Puzzle Program 138
sequence = [1,2,3,4,5]
for loop in range(4):
    temp = sequence.pop(0)
    sequence.append(temp)
print(sequence)