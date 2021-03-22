## Counting Weeds
## Program 54
## With comments

## Set up a 2D list of quadrat boxes with 5 rows and 5 columns.
## Each element is assigned the value 0.
quadrat = [[0] * 5 for main in range(5)]

## Initialse a variable to store the total number of weeds.
total = 0

## Enter the number of weeds at each coordinate in turn.
## Note that the user sees the coordinates as rows 1 to 5 and
## columns 1 to 5. Adding 1 to each outer and inner loop value
## when displaying the rows and column coordinates is required

for outer in range(5):
    for inner in range(5):
        quadrat[outer][inner] = int(input("Please enter the number of weeds counted at "+str(outer+1)+","+str(inner+1)+":"))
        total = total + quadrat[outer][inner]

## Display the quadrat 2D list.
for outer in range(5):
    for inner in range(5):
        print(quadrat[outer][inner],"",end=' ')
    print()

## Display the total number of weeds.
print("The total number of weeds found was -",total)