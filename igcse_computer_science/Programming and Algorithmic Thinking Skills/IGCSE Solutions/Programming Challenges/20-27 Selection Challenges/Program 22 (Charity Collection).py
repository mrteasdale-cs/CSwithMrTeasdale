## Charity Collection
## Program 22
## With Comments

## The user is asked to input three amounts of money raised so
## three inputs required:

first = int(input("Please enter the first amount of money raised."))
second = int(input("Please enter the second amount of money raised."))
third = int(input("Please enter the third amount of money raised."))

## The program then calculates and stores the total.

total = first + second + third

## The total is then displayed.  Note to position the £ symbol next
## to the amount raised we must use concatenation (and therefore convert
## the total to a string).

print ("A total of £"+str(total),"was raised.")

## The program then displays a second message if the total is greater
## than or equal to 1000.  Note that in this second message the total raised
## is multiplied by 2.

if total >= 1000:
    print ("This will be doubled to £"+str(total*2))

