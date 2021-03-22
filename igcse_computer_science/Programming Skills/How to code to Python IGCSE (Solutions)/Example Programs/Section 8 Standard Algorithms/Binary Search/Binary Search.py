# Standard Algorithm
# Merge Sort (Python version using pop() function)

def binarysearch(nameList,target):
    lower = 0
    upper = len(nameList)-1

    while lower<=upper:
        mid = int((lower+upper)/2)
        if nameList[mid] == target:
            return mid
        elif nameList[mid] < target:
            lower = mid + 1
        else:
            upper = mid - 1

    return -1

names = ["Aaron","Beth","Clive","Dennis","Egbert","Francis","Gillian","Hugh","Icarus","Jeremy","Kyle","Lachina"]
ages = [33,56,34,56,75,34,24,87,34,44,50,40]
toFind = str(input("Enter a name"))
position = binarysearch(names,toFind)
if position>=0:
    print(names[position],"is",ages[position],"years old")
else:
    print("Name not found")