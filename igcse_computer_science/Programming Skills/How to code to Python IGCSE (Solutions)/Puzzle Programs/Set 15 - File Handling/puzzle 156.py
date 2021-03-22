# Puzzle Program 156

bikes = ["Carrera","Ridgeback","Boardman","Giant"]
count = 1
with open('bikes.txt','w') as bikeFile:
    for each in bikes:
        bikeFile.write(str(count) + ". " + each + "\n")
        count = count + 1