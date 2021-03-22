# Puzzle Program 157

sizes = ["12","23","16","08"]
moreSizes = ["10","20",]
with open('sizes.txt','w') as sizeFile:
    for each in moreSizes:
        sizeFile.write(str(each)+"\n")
with open('sizes.txt','a') as sizeFile:
    for each in sizes:
        sizeFile.write(str(each)+"\n")