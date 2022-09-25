# Standard Algorithm
# Bubble Sort (Simple Function returning sorted list)

def bubbleSort(sortList):
    for outerLoop in range(0,len(numbers)-1):
        for innerLoop in range(0,len(numbers)-1):
            if sortList[innerLoop] > sortList[innerLoop+1]:
                temp = sortList[innerLoop]
                sortList[innerLoop] = sortList[innerLoop+1]
                sortList[innerLoop+1] = temp
    return sortList

numbers = [7,3,1,86,99,12,4]
print(bubbleSort(numbers))