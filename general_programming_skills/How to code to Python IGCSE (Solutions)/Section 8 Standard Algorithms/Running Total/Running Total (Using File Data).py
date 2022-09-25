# Standard Algorithm
# Running Total (Reading from File)

def runningTotal(fileName):
    total = 0
    fileName = fileName + ".txt"
    with open(fileName) as nums:
        for each in nums.readlines():
            each = each[0:-1]
            total = total + int(each)
    return total


fileName=str(input("Which file would you like to add up?"))
total = runningTotal(fileName)
print("The total =",total)