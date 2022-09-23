months =  ["January", "February", "March", "April",
           "May", "June", "July", "August",
           "September", "October", "November", "December"]

rainfall = [0]*12
annualRainfall = 0

for i in range(0,12):
    print("Please input rainfall for month " + months[i] + ": ")
    rainfall[i] = float(input())
    annualRainfall = annualRainfall + rainfall[i]

averageRainfall = annualRainfall / 12

# statement below is equivalent to monthsAboveAverage = monthsAboveAverage + 1
monthsAboveAverage = 0

for i in range(0,12):
    if rainfall[i] > averageRainfall:
        monthsAboveAverage += 1
    
    print(months[i] + str(rainfall[i]))

print("Annual rainfall = " + str(annualRainfall))
print("Average monthly rainfall = " + str(averageRainfall))
print("Number of months above average rainfall = " + str(monthsAboveAverage))
