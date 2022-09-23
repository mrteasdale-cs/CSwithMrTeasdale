#read a text file
#reads the film file, which is in the same folder,
#and prints all eight records


filmFile = open("Films.txt","r")   #"r" opens the file for reading
print("The film file has been opened for reading")
filmRec = filmFile.readline()      #read the first record
for n in range(8):
    filmRec = filmFile.readline()      #read a record
    print (filmRec)
filmFile.close()
    
  

