## Press up Challenge
## Program 35
## With Comments

## The user is then asked to enter the number of students.

students = int(input("Please enter the number of students."))

## A single message is displayed and the the program loops for
## each student.  Note how the loop variable is used to display which
## student time is being asked for.
## A running total adds up the times.

totalTime = 0
print("Enter the time in seconds for each student.")
for loop in range(students):
    time = int(input("Student "+str(loop+1)))
    totalTime += time     ## This is a shortcut way of writing totalTime = totalTime + time

## The average time is then calculated by dividing the total by the number of students.

averageTime = totalTime / students

## The average is displayed to 2 decimal places.

print("The average time for the "+str(students)+" students was:")
print(round(averageTime,2),"seconds")
