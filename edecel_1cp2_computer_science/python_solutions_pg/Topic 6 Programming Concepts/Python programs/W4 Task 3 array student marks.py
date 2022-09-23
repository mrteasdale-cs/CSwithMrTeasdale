name = [""]*3
total = [0]*3
averageMark = [0]*3
mark = [
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]
        ]
for student in range(3):
    name[student] = input("Enter student name: ")
    for m in range(5): 
       print("Enter mark",m+1,": ")
       mark[student][m] = int(input())
       total[student] = total[student] + mark[student][m]
    
    print("Total for student",name[student], total[student])
    averageMark[student] = round(total[student]/5,1)
    print("Average mark for ",name[student], averageMark[student])
    
input("\nPress ENTER to exit program ")
