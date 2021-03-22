## Meal Vouchers
## Program 60
## With Comments

## Initialise two parallel 1D lists to store ages and seats as
## audience members are entered.
ages = []
seats = []

## Start a conditional loop that end when the user enters N
another = "Y"
while another.upper() == "Y":

    ## Get valid inputs from user.
    nextAge = int(input("Enter age:"))
    while nextAge<0 or nextAge>100:
        nextAge = int(input("Please enter an age between 0 and 100"))

    nextSeat = int(input("Enter seat:"))
    while nextSeat<1 or nextSeat>56:
        nextSeat = int(input("Please enter a seat number between 1 and 56"))

    ## Append the above values to the two lists.
    ages.append(nextAge)
    seats.append(nextSeat)

    ## Ask the user if they wish to enter another audience member.
    another = str(input("Do you wish to enter another:"))
    ## validate the input as only two choices should be entered
    while not(another.upper() == "Y" or another.upper() == "N"):
        another = str(input("Please enter only Y or N"))

## Find the largest age stored in the list.
maxAge = max(ages)

## Now find the index of the element where this value first appears
## in the list.
ageIndex = ages.index(maxAge)

## Display the result.
print("The oldest audience member is sitting in seat",seats[ageIndex])

## Count and display the number of ages entered as 0
print(ages.count(0),"audience members did not give their age.")


## Note that three of the last lines could be combined into one.
## As your programming improves you will see more of these shortcuts.
## print("The oldest audience member is sitting in seat",seats[ages.index(max(ages))])