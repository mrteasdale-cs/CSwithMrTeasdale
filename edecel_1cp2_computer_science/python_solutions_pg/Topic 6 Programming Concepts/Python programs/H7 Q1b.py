boxVolumes = [] #used to store the volumes of the boxes

for i in range(4):
    #get measurements from user
    length = int(input("Enter length: "))
    height = int(input("Enter height: "))
    depth = int(input("Enter depth: "))
    
    volume = length * height * depth #calculate volume
    print(volume)
    boxVolumes.append(volume) #append volume to boxVolumes
    
print(boxVolumes)
