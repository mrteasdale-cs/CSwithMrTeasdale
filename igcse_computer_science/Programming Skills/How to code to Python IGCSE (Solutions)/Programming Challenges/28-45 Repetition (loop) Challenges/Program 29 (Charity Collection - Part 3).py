## Charity Collection - Part 3
## Program 29
## With Comments

## The first part of the program remains the same as before.

first = int(input("Please enter the first amount of money raised."))
second = int(input("Please enter the second amount of money raised."))
third = int(input("Please enter the third amount of money raised."))

total = first + second + third

print ("A total of £"+str(total),"was raised.")

## To display the message and the total x 3 the output has to be
## split into two different print statements.  The second print
## statement is placed inside a loop to display 3 times

if total < 1000:
    print ("This final total raised is:")
    for loop in range(3):
        print("£"+str(total+100)+"!!!")
elif total >= 1000 and total <= 2000:
    print ("The company will double the total to:")
    for loop in range(3):
        print("£"+str(total*2)+"!!!")
else:
    print ("With the company bonus, this is:")
    for loop in range(3):
        print("£"+str(4000+total-2000)+"!!!")


## NOTE
## Rather than having three separate pairs of print statements it
## would be more efficient to store each message and then loop
## once like this:

## if total < 1000:
##     print ("This final total raised is:")
##     finalTotal = "£"+str(total+100)+"!!!"
## elif total >= 1000 and total <= 2000:
##     print ("The company will double the total to:")
##     finalTotal = "£"+str(total*2)+"!!!"
## else:
##     print ("With the company bonus, this is:")
##     finalTotal = "£"+str(4000+total-2000)+"!!!"
## for loop in range(3):
##     print(finalTotal)
