## Horse Hands
## Program 50
## With comments

## The program stores the details 8 horses
names = ["Black Beauty","Red Run","Bess","Derek","Philis","Mental","Sissy","Canter","Francine","Langrish"]
ages = [12,18,8,5,10,13,19,14,8,15]
height = [13,14,12,15,16,18,14,15,14,14]

## The maximum age and height are input by the user
maxAge = int(input("Please enter the maximum age of the horse"))
maxHeight = int(input("Please enter the maximum height of the horse"))

print("Suitable horses are:")

## A loop traverses each element of the lists
for loop in range(10):
    ## The details of a horse are only displayed if the conditions of the
    ## if statement are met (age is less than or equal to the inputted age and
    ## the height is less than or equal to the inputted height)
    if ages[loop] <= maxAge and height[loop] <= maxHeight:
        print (names[loop]+",",ages[loop],"years ,"+str(height[loop]),"hands")
