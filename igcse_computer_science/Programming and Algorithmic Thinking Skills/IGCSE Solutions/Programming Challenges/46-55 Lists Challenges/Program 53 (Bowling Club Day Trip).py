## Bowling Club Day Trip
## Program 53
## With comments

## Set up a 2D list of bus seats with 5 rows and 4 columns.
## Each element is assigned the string "Empty".  As the members
## names are entered later these strings will be replaced
seats = [["Empty"] * 4 for main in range(5)]

## Ask how many members need a seat.  This can be used in the
##  fixed loop below.

numMembers = int(input("How many members have requested a seat?"))

## Use a loop to ask if each person is attending
for loop in range(numMembers):
    name = str(input("Please enter your name."))

    ## Get the row and seat number.
    ## These should be validated as using an index less than 0
    ## or more than the index values in the 2D list would cause
    ## an error.
    row = int(input("Which row would you like to sit in?"))
    while row<0 or row>4:
        print("Row must be between 0 and 4")
        row = int(input("Which row would you like to sit in?"))

    seat = int(input("Which seat would you like to sit in?"))
    while seat<0 or seat>3:
        print("seat must be between 0 and 3")
        seat = int(input("Which seat would you like to sit in?"))

    ## The row and seat are now used as indexes in the 2D list
    ## to store the member's name.
    seats[row][seat] = name



## Display the bus seats.
## Note how end=' ' is used along with print() to display the seat
## information on the same line or a new line.
for outer in range(5):
    print(str(outer)+". ",end=' ')
    for inner in range(4):
        print(seats[outer][inner],"",end=' ')
    print()
