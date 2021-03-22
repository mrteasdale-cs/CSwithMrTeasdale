# Puzzle Program 160

presidents = []
with open('presidents.txt','r') as pres:
    for each in pres.readlines():
        each = each[0:-1]
        presidents.append(each)
for loop in range(len(presidents)):
    print(presidents[loop])