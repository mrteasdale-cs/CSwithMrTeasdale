## Program 49
## Dance Group
## With Comments

## Empty list are set up to store the four names and ages.
ages = [0]*4
names = [""]*4

## To input multiple values into a list a loop should be used.
## The loop variable (in this example, counter) is used to ensure
## each input is stored in a different element of the list.
for counter in range(4):
    names[counter] = (input("Please enter a name"))
    ages[counter] = int(input("Please enter "+names[counter]+"'s age"))

## A second loop is used to display the names along with each dancers
## group.  An complex if statement ensure the correct group is displayed.
print("Names and Competition List:")
for counter in range(4):
    if ages[counter] < 12:
        print(names[counter],"-","Junior")
    elif ages[counter] >= 12 and ages[counter]<18:
        print(names[counter],"-","Teen")
    elif ages[counter] >= 18:
        print(names[counter],"-","Senior")
