#multiple choice quiz question

print("What is the world's largest ocean?  ")
print("1. Atlantic\n2. Pacific\n3. Indian")
answer = input("Answer 1, 2 or 3: ")
if answer == "2":
    print ("Correct!")
else:
    print ("No, it's the Pacific")







#Homework 2 Qu 2 Leap Year

year = int(input("Please enter a year: "))
leapYear=False
if (year%4)==0:
    leapYear = True
if (year%100)==0:
    leapYear = False
if (year%400)==0:
    leapYear = True
if leapYear == True:
    print ("That is a Leap Year")
else:
    print ("That is not a Leap Year")

