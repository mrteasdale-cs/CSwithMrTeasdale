
import random
#die1 = random.randint(1,6)
#die2 = random.randint(1,6)
#die3 = random.randint(1,6)
for n in range(5):
#for testing purposes, input values for die1, die2 and die3
    die1 = int(input("die1: "))
    die2 = int(input("die2: "))
    die3 = int(input("die3: "))

    score = 0
    if die1 == die2 and die1 == die3:     #3 equal dice
        score = die1 +die2 + die3
    elif die1 == die2:  #2 equal dice
        score = die1 + die2 - die3
    elif die1 == die3:  #2 equal dice
        score = die1 + die3 - die2
    elif die2 == die3:  #2 equal dice
        score = die2 + die3 - die1    
    else:
        score = 0 
    print("Score = ",score)
print("End of program")

input("Press Enter to exit ")
    
