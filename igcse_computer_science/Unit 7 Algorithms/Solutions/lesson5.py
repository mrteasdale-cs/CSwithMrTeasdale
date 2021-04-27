#Worksheet Task 2
# Mighty Max
wounds=0
gremlins=4
strength=30

while strength >0:
    if gremlins >= 1:
        wounds = wounds+gremlins
    if strength > 2:
        gremlins = gremlins-1
        print ("Mighty Max has dealt a deathly blow to a gremlin, but his strength is fading")
    strength = strength-wounds    
    print ("Wounds = ",wounds, "gremlins = ",gremlins, "   Strength = ", strength)
    continuegame = input("Press any key")
print ("Alas, our hero has been overcome... Game Over")


#worksheet 1 Task 3
#Dice game1

import random
#die1 = random.randint(1,6)
#die2 = random.randint(1,6)
#die3 = random.randint(1,6)
for n in range(8):
#for testing purposes, input values for die1, die2 and die3
    die1=int(input("die1: "))
    die2=int(input("die2: "))
    die3=int(input("die3: "))

    score = 0
    if die1 == die2 and die1 == die3:     #3 equal dice
        score = die1 +die2 + die3
    elif die1 == die2 and  die1 != die3:  #2 equal dice
        score = die1 + die2 - die3
    elif die1 == die3 and die2 != die3:  #2 equal dice
        score = die1 + die3 - die2
    elif die2 == die3 and die1 != die3:  #2 equal dice
        score = die2 + die3 - die1    
    else:
        score = 0 
    print ("Score = ",score)
print ("End of program")


#Worksheet Task 3
#grains of wheat
print("How many grains of wheat will be on each square?")
powerOf2 = 1
total = 1
for n in range(2,7):
    powerOf2 = powerOf2*2
    total = total + powerOf2
    print("You have a total of ",total, "grains on squares 1 to",n)

#HOMEWORK

# homework 5 question 1
# The program finds the maximum and minimum numbers in an array x
# It also finds the total of all the numbers in the array
# It then outputs the maximum and minimum
# Then it subtracts these values from the total,
# calculates the average of the remaining numbers in the array
# Converts this to an integer value and outputs the result

x = [7, 9, 6, 2, 4]
n = 0
t = x[0]
k = x[0]
j = x[0]
print("t, k, j, n, x[n] ", t,k,j,n,x[n])
for n in range(1,5):
    t = t + x[n]
    if x[n] >k:
        k = x[n]
    if x[n] <j:
        j = x[n]
    print("t, k, j, n, x[n] ", t,k,j,n,x[n])

t = t-k-j
print("k = ",k,"  j = ",j, "t = ",t)
a = t/3
a = int(a)
print ("a = ", a)



#pass or distinction
mark = 0
studentPass = 0
distinction = 0
numStudents = 0
totalMark = 0
while mark!= -1:
    print("Please enter mark, -1 to end: ")
    mark = int(input())
    if mark>=50:
        studentPass = studentPass + 1
    else:
        if mark >= 80:
            distinction = distinction + 1
    numStudents = numStudents + 1
    totalMark = totalMark + 1
averageMark = totalMark/numStudents
    
print ("Number of students: ", numStudents)
print ("Number of students with pass or distinction: ", studentPass) 
print ("Number of students with distinction: ", distinction)
print("Average mark: ",averageMark)


