# Standard Algorithm
# Find Maximum (Function Example)

def findMaximum(maxlist):
    maximum = maxlist[0]
    for counter in range(1,len(maxlist)):
        if maxlist[counter] > maximum:
            maximum = maxlist[counter]
    return maximum

numbers = [12,3,5,4,67,7,5,3,5,7,1]
print("Maximum value is:",findMaximum(numbers))