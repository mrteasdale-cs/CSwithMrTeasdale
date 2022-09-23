#reads and and prints names and marks of all students who scored a mark >79
#open file for reading and print students with marks > 79
marksFile = open("marks.txt", "r")

print("\nListed below are students with a mark of 80 or more")

moreLines = True
while moreLines:
    markRec = marksFile.readline()
    if markRec == "":
        moreLines = False
    else:
        #The next statement splits the record into field[0], field[1]
        field = markRec.split(",")          #fields are separated by commas
        name = field[0]
        mark = int(field[1])
        if mark >= 80:
            print(name, mark)

marksFile.close()

input("\nPress ENTER to exit program ")
    
    

