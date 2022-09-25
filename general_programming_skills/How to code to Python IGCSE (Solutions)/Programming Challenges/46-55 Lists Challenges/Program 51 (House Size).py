## House Size
## Program 44
## With comments

## First ask for the number of rooms...
noOfRooms = int(input("Please enter the number of rooms in the house"))

## ...as this can be used to set the required lists to the correct size.
roomName = [""]* noOfRooms
length = [0.0]* noOfRooms
width = [0.0]* noOfRooms

## Each room area will be added onto this variable later.
totalArea = 0.0


## A loop is used to input the details of each room.
for rooms in range(noOfRooms):
    roomName[rooms] = str(input("Please enter the name of room "+str(rooms+1)))
    length[rooms] = float(input("Please enter the length (m) of room "+str(rooms+1)))
    width[rooms] = float(input("Please enter the width (m) of room "+str(rooms+1)))

print("House details:")

## A loop is used to display the name and area (calculated from width*length)
## of each room.  Note that round() is used to display the area to 1 decimal place.
for rooms in range(noOfRooms):
    print("Room -",roomName[rooms])
    areaRoom = length[rooms] * width[rooms]
    print(round(areaRoom,1),"metres squared")
    totalArea = totalArea + areaRoom

## The running total above adds each calculated area onto a total which is
## then displayed below.
print("The total area is calculated as:")
print(round(totalArea,1),"metres squared")