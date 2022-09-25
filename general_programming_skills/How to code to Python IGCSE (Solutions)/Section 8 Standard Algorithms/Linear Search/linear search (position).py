# Standard Algorithm
# Linear Search

def checkNames(target,nameList):
    index = -1
    for names in range(len(nameList)):
        if nameList[names] == target:
            index = names
    return index

names = ["Najwa","Mary","Shandra","Batya","Aisling"]
targetName =str(input("Enter a name"))
position = checkNames(targetName,names)
if position >= 0:
    print(names[position],"found in list")
    print("at position:",position)
else:
    print("Name not found")