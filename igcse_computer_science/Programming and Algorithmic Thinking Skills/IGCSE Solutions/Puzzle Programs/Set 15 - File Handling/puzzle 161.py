# Puzzle Program 161
presidents = ["James Monroe","John Quincy Adams"]

with open('presidents.txt','r') as pres:
    for each in pres.readlines():
        presidents.append(each[0:-1])

for loop in range(len(presidents)):
    print(str(loop+1)+". "+presidents[loop])