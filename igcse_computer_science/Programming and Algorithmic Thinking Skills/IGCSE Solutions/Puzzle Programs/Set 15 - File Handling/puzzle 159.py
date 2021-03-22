# Puzzle Program 159

elements = []
with open('elements.txt','r') as elem:
    for each in elem.readlines():
        print(each[0:-1])
