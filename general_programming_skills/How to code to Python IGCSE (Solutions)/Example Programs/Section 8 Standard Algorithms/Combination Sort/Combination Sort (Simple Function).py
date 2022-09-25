# Standard Algorithm
# Combining Two Sorted Lists (Function returning sorted list)
# Note that  this was originally in the book but was removed due to lack
# of space.  I left it in as it's a fun algorithm.

def combinationSort(list1,list2):
    index1 = 0
    index2 = 0
    list3 = []
    while index1!=len(list1) or index2!=len(list2):
        if index1 == len(list1):
            list3.append(list2[index2])
            index2 += 1
        elif index2 == len(list2):
            list3.append(list1[index1])
            index1 += 1
        else:
            if list1[index1] <= list2[index2]:
                list3.append(list1[index1])
                index1 += 1
            else:
                list3.append(list2[index2])
                index2 += 1
    return list3

numbersOne = [1,8,9,10,13,15,16,20]
numbersTwo = [4,7,12,13,13,14]
sortedList = combinationSort(numbersOne,numbersTwo)
print(sortedList)