userName = ["Carl","Tamsin","Eric","Zoe","Alan","Mark"]
numItems = len(userName)
for i in range(0,numItems - 1):
    for j in range(0, numItems - i - 1):
        if userName[j] > userName[j+1]:
            temp = userName[j] 
            userName[j] = userName[j+1] 
            userName[j+1] = temp

print(userName)
