## Charity Collection - Part 2
## Program 27
## With Comments

## The first part of the program remains the same as before.

first = int(input("Please enter the first amount of money raised."))
second = int(input("Please enter the second amount of money raised."))
third = int(input("Please enter the third amount of money raised."))

total = first + second + third

print ("A total of £"+str(total),"was raised.")

## The program then uses a complex if statement to display
## multiple messages each of which has a different calculation.

if total < 1000:
    print ("This final total raised is £"+str(total+100)+".")
elif total >= 1000 and total <= 2000:
    print ("The company will double the total to £"+str(total*2)+".")
else:
    print ("With the company bonus, this is £"+str(4000+total-2000)+".")

