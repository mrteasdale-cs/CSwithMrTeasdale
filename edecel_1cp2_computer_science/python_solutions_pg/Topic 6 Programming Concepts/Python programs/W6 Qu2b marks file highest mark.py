marksFile = open("marks.txt", "r")

moreLines = True
maxMark = 0
student = ""
while moreLines:
    markRec = marksFile.readline()
    if markRec == "":
        moreLines = False
    else:
        field = markRec.split(",")
        name = field[0]
        mark = int(field[1])
        if mark > maxMark:
            student = name
            maxMark = mark

print(student, maxMark)
marksFile.close()

