# Standard Algorithm
# Count Occurence (Reading from File)

def countOccurrence(fileName,targetNumber):
    occurrence = 0
    fileName = fileName + ".txt"
    with open(fileName) as nums:
        for each in nums.readlines():
            each = each[0:-1]
            if int(each) == targetNumber:
                occurrence = occurrence + 1
    return occurrence

file = "numbers"
target=int(input("State the value to count"))
total = countOccurrence(file,target)
print(target,"appeared",total,"times")