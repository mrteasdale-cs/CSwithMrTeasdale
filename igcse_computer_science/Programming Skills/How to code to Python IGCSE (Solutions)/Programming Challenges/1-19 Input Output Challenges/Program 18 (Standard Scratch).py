## Standard Scratch
## Program 18
## With Comments

## The user is asked to input four pieces of information about
## the golf course.  Four inputs are therefore required.

par3s = int(input("How many par 3 holes are there?"))
par4s = int(input("How many par 4 holes are there?"))
par5s = int(input("How many par 5 holes are there?"))
difficulty = int(input("What is the difficulty adjustment for the course?"))

## The program then adds up the total number of shots for the course.

totalShots = (par3s*3) + (par4s*4) + (par5s*5)

## The standard scratch is the total + the difficulty of the course

standardScratch = totalShots + difficulty

## The output is shown on two lines so two print() statements are required.

print ("The Standard Scratch for the course is:")
print(standardScratch)

