marksFile = open("marks.txt", "a")
print("This program lets you write names and marks to marks.txt")
print("If the file does not exist, it will be created")

moreNames = True
while moreNames:
    name = input("Enter student name: ")
    mark = input("Enter student mark: ")
    marksFile.write(name + "," + mark + "\n")
    if input("Add another student (y/n)? ") == "n":
        moreNames = False

marksFile.close()


    
    

