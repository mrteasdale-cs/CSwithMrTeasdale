# Standard Algorithm
# Insertion Sort (Function returning sorted list)

def insertionSort(values):
    for index in range(1,len(values)):
        currentscore = values[index]
        position = index
        while position>0 and values[position-1]>currentscore:
            values[position]=values[position-1]
            position = position-1
        values[position]=currentscore
    return values

numbers = [7,1,10,26,4,5]
print(insertionSort(numbers))