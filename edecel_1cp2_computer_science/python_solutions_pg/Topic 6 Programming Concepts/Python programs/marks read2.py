marksFile = open("marks.txt","r")
marks = marksFile.readlines()
for i in range(len(marks)):
   print(marks[i])
marksFile.close()


