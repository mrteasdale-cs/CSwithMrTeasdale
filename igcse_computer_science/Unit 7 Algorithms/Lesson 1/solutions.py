# total > 500
total = 0
n = 0
while not (total > 500):
    n = n + 1
    total = total + n
print ("n = ", n,"  total = ",total)

#######################
#worksheet 1 Task 3
#Dice game1

import random
#die1 = random.randint(1,6)
#die2 = random.randint(1,6)
#die3 = random.randint(1,6)
for n in range(5):
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

#newtask
    
import random
anotherGo = "y"
score = 0
while  anotherGo != "n":
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print ("die 1, die 2 = ",die1, "  ", die2)
    if die1 == die2:
        anotherGo = 'n'
        score = 0
        print ("Score = ", score) 
    else:
        score = score + die1 + die2
        print ("Score = ", score)
        anotherGo = input ("Another go? (y or n): ")
print ("Final Score = ", score)

# total > 500
total = 0
n = 0
while not (total > 500):
    n = n + 1
    total = total + n
print ("n = ", n,"  total = ",total)

MealCost = float(input(“Enter the meal cost”))
DrinkCost = float(input(“Enter the drink cost”))
WeeklyTotal = MealCost + (2 * drinks) * 5
Print (WeeklyTotal)


################

#worksheet 1 Task 3
#Dice game2

import random
anotherGo = "y"
score = 0
while  anotherGo != "n":
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print ("die 1, die 2 = ",die1, "  ", die2)
    if die1 == die2:
        anotherGo = 'n'
        score = 0
        print ("Score = ", score) 
    else:
        score = score + die1 + die2
        print ("Score = ", score)
        anotherGo = input ("Another go? (y or n): ")
print ("Final Score = ", score)






