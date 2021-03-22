# Standard Algorithm
# Combining Two Sorted Lists (Python version using pop() function)
# Note that  this was originally in the book but was removed due to lack
# of space.  I left it in as it's a fun algorithm.

def combinationSort(list1,list2):
    list3 = []
    while len(list1)>0 or len(list2)>0:
        if len(list1)==0:
            list3.append(list2.pop(0))
        elif len(list2)==0:
            list3.append(list1.pop(0))
        else:
            if list1[0] <= list2[0]:
                list3.append(list1.pop(0))
            else:
                list3.append(list2.pop(0))
    return list3

numbersOne = [1,8,9,10,13,15,16,20]
numbersTwo = [4,7,12,13,13,14]
sortedList = combinationSort(numbersOne,numbersTwo)
print(sortedList)