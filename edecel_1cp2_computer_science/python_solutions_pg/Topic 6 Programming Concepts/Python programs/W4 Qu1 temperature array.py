months =  ["January", "February", "March", "April",
           "May", "June", "July", "August", "September",
           "October", "November", "December"]

#Temperature =[0,0,0,0,0,0,0,0,0,0,0,0]  can be written as
temperature = [0]*12

for i in range(0,12):
    print("Enter temperature for month", months[i])
    temperature[i] = int(input())

for i in range(0,12):
    print(months[i], "  ", temperature[i])
