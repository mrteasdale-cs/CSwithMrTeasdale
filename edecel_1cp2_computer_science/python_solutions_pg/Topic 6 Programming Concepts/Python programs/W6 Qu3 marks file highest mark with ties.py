marksFile = open("marks.txt", "r")


moreLines = True
maxMark = 0
students = []
while moreLines:
    markRec = marksFile.readline()
    if markRec == "":
        moreLines = False
    else:
        field = markRec.split(",")
        name = field[0]
        mark = int(field[1])
        if mark == maxMark:
            students.append(name)
        elif mark > maxMark:
            students = [] #empty the list
            students.append(name)
            maxMark = mark

marksFile.close()
            
for i in range(len(students)):
    print(students[i], maxMark)


input("\nPress ENTER to exit program ")
    
    

  

