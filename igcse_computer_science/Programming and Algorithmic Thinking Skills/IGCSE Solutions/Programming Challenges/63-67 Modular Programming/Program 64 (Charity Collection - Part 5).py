## Charity Collection - Part 5
## Program 64
## With Comments

## The program should be edited to have one function and one procedure.

## The function adds up the amount raised and returns the result.
def calculateTotal(numValues):
    total = 0
    print ("Enter the total raised by each.")
    for amounts in range(numValues):
        money = int(input())
        total = total + money
    return total

## The procedure displays the messages as with Charity Collection - Part 4.
def displayMessages(totalRaised):
    print ("A total of £"+str(totalRaised),"was raised.")

    if totalRaised < 1000:
        print ("This final total raised is:")
        for loop in range(3):
            print("£"+str(totalRaised+100)+"!!!")
    elif totalRaised >= 1000 and totalRaised <= 2000:
        print ("The company will double the total to:")
        for loop in range(3):
            print("£"+str(totalRaised*2)+"!!!")
    else:
        print ("With the company bonus, this is:")
        for loop in range(3):
            print("£"+str(4000+totalRaised-2000)+"!!!")


## Main Program
people = int(input("How many charity raisers were there?"))

## call the function that calculates and returns the total raised.
total = calculateTotal(people)

## Call the procedure that displays the final messages.
displayMessages(total)


## Note: This problem is really about reorganising code that you
## have already.  From now on you should try and write your programs
## with a small Main Program that calls functions and procedures
## that carry out sub-tasks.

