# Puzzle Program 163
names = []
jump = []

with open('longJumps.txt','r') as longJs:
    for eachPerson in longJs.readlines():
        eachPerson = eachPerson[0:-1]
        temp = eachPerson.split("-")
        names.append(temp[0])
        longest = max(float(temp[1]), float(temp[2]), float(temp[3]), float(temp[4]))
        jump.append(longest)

for loop in range(len(jump)):
    print(names[loop],jump[loop])
