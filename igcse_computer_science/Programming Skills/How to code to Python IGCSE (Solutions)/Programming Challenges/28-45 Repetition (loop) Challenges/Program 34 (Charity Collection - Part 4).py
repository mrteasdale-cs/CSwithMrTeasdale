## Charity Collection - Part 4
## Program 34
## With Comments

## The program first asks for the number of charity raisers.

people = int(input("How many charity raisers were there?"))

## It then diaplays a message and loops the number of times entered.
## Each repetition asks for an amount to be entered.
## Within the loop a running total is used to add up the amounts entered.

total = 0
print ("Enter the total raised by each.")
for amounts in range(people):
    money = int(input())
    total = total + money

## The rest of the program remains the same as before.

print ("A total of £"+str(total),"was raised.")

if total < 1000:
    print ("This final total raised is:")
    for loop in range(3):
        print("£"+str(total+100)+"!!!")
elif total >= 1000 and total <= 2000:
    print ("The company will double the total to:")
    for loop in range(3):
        print("£"+str(total*2)+"!!!")
else:
    print ("This will be increased to:")
    for loop in range(3):
        print("£"+str(4000+total-2000)+"!!!")
