# Puzzle Program 164
temp1List = []
temp2List = []

with open('num1.txt','r') as numbers:
    for eachNum in numbers.readlines():
        eachNum = eachNum[0:-1]
        temp = eachNum.split(",")
        temp1List.append(temp)
with open('num2.txt','r') as numbers:
    for eachNum in numbers.readlines():
        eachNum = eachNum[0:-1]
        temp = eachNum.split(",")
        temp2List.append(temp)
with open('num3.txt','w') as numbersOut:
    for loop in range(0,2):
        numbersOut.write(str(temp1List[loop][0])+"\n")
    for loop in range(2,4):
        numbersOut.write(str(temp2List[loop][3])+"\n")

total = 0
with open('num3.txt','r') as numbers:
    for eachNum in numbers.readlines():
        total = total + int(eachNum[0:-1])

print("Total =",total)
