## Garage Sales
## Program 69
## With comments

## The procedure below is passed two values which it writes to a text
## file, called 'garage.txt', separated by a comma.
def addToFile(text,number):
    with open('garage.txt','a') as hairColourFile:
        hairColourFile.write(text + ","+str(number) + "\n")


## This standard procedure opens a read only connection to the
## garage.txt file and displays its contents.
def displayItems():
    with open('garage.txt','r') as items:
        for each in items.readlines():
            each = each[0:-1]
            temp = each.split(",")
            print(temp[0],"£"+temp[1])


## MAIN PROGRAM
description = ""
price = 0

## Keep asking for items until the user enters X
while not(description.upper() == "X"):
    description = str(input("Please enter description"))

    if description.upper() != "X":
        ## Get valid price.
        price = float(input("Please enter the price"))
        while price < 0:
            price = int(input("Please reenter a valid price >= 0"))

        addToFile(description,price)

## Call the procedure to display the file data.
displayItems()


## Extension Task
## Ensure the prices always display with two decimal places.


