# Standard Algorithm
# Linear Search

def checkNames(target,nameList):
    found = False
    for names in nameList:
        if names == target:
            found = True
    return found

names = ["Najwa","Mary","Shandra","Batya","Aisling"]

targetName =str(input("Enter a name"))
result = checkNames(targetName,names)
if result:
    print("Name found in list")
else:
    print("Name not found")