## Who's Going to the Party?
## Program 52
## With comments

## Set up two lists.  One for all the names. One to store whether
## or not an invitation has been accepted.
## Note that the second list is a list of booleans and all 10 elements
## are initially set to False.
names = ["Mellisa","Evelyn","Emmy","Karen","Margaret","Norma","Agnes","Billy","Robert","Arthur"]
accept = [False]*10

print("Who's Going?")

## Use a loop to ask if each person is attending
for loop in range(10):
    print(names[loop]+"?")
    yesNo = str(input())
    ## If the user enters Y or y the appropraite element is changed to
    ## store True in the boolean list
    if yesNo == "Y" or yesNo == "y":
        accept[loop] = True

print("Party Attendance List:")

## A second loop displays names elementsh where the matching accept list element
## stores the value "True".
for loop2 in range(10):
    if accept[loop2] == True:
        print(names[loop2])
