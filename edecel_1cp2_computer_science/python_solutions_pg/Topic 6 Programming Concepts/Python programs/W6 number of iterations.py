names = ["Anna", "Bill", "Faisal", "Pavel", "Tom"]
ages = [14, 16, 14, 17, 15]
year = [10, 11, 9, 13, 10]

#Algorithm 1
records = []
for i in range(len(names)):
    records.append([names[i], ages[i], year[i]])
print(records)

#Algorithm 2
namesAges = []
allDetails = []
for i in range(len(names)):
    namesAges.append([names[i], ages[i]])
for i in range(len(names)):
    namesAgesRecord = namesAges[i]
    namesAgesRecord.append(year[i])
    allDetails.append(namesAgesRecord)
print(allDetails)
    
