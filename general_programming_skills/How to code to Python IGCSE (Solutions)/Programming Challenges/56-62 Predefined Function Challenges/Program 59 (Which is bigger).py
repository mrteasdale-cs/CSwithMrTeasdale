## Which is Bigger?
## Program 59
## With Comments

## Import the random library as random integers are required later.
import random

## Set the users correct guesses to 0.
total = 0

for loop in range(10):
    ## generate two random numbers between 1 and 1000
    num1 = random.randint(1,1000)
    num2 = random.randint(1,1000)

    ## Ask the user to guess if num1 or num2 is the larger number
    print("I have generated two random numbers")
    choice = int(input("Which is largest, 1 or 2?"))
    ## validate the input as only two choices should be entered
    while choice<1 or choice>2:
        choice = int(input("Please enter only 1 or 2"))

    print("Number 1 =",num1)
    print("Number 2 =",num2)
    ## Add 1 to users correct guess score if they are correct.
    if choice == 1 and num1>num2:
        print("Correct, number 1 was the larger")
        total += 1
    elif choice == 2 and num1<num2:
        print("Correct, number 2 was the larger")
        total += 1
    else:
        print("Sorry, wrong guess")

## Display the users final score.
print("Your total was",total,"correct guesses out of 10")
print("Your final score was",total,"correct")
