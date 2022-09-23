year = int(input("Please enter a year: "))
leapYear = False

if (year % 4) == 0:
    leapYear = True
if (year % 100) == 0:
    leapYear = False
if (year % 400)== 0:
    leapYear = True
    
if leapYear:
    print ("That is a Leap Year")
else:
    print ("That is not a Leap Year")
