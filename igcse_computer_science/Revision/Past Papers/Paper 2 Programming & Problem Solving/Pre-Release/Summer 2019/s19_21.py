'''Task 1 – Setting up the data storage.
Using arrays set up a system to enable data for each bus route to be entered covering each day of a four-week period. It must be
possible to enter the data supplied or your own set of data, using suitable prompts as necessary.'''
import random
from array import *
'''Task 1 – Setting up the data storage.
Using arrays set up a system to enable data for each bus route to be entered covering each day of a
four-week period. It must be possible to enter the data supplied or your own set of data, using suitable
prompts as necessary.'''
#timetable = [[], [], [], [], [], [],[], [], [], [], [], [], [], [], [], [], [], [],[], [], [], [], [], []]
timetable = [[],[]]*2
#bus_a = []

print(timetable)
buses = ["A","B","C","D","E","F"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

for day in range(0, 2):

    for bus in range(0, 6):
        minutes = int(input(f"Enter the minutes for bus {buses[bus]} on {days[day]}{(day+1)} ".format(buses[bus],days[day],day)))
        timetable[day].insert(bus, minutes)

print(timetable)

'''Task 2 – Working out the statistics.
Extend your program so that the following statistics for the four-week period may be calculated and
output:
• the number of late arrivals for each bus route
• the average number of minutes late for each bus route
• the bus route with the highest number of days on which it was late
• the average number of minutes late for each bus route, using only data from days on which it was
late. All the results should be displayed with appropriate annotation.'''
# Statistics
def getStats():
    averageList = []
    lateList = []
    for bus in range(len(timetable)):
        total = 0
        late = 0
        for day in range(len(timetable[bus])):
            avg = len(timetable[bus])
            currentTime = timetable[bus][day]
            # Check if late
            if currentTime < 0:
                late += 1
                # Average
                total += timetable[bus][day]
        if late > 0:
            result = total / late
            lateList.append(late)
            averageList.append(round(result,2))

    return lateList, averageList


def printing(busList, dayList):
    results = getStats()
    print(results)
    if len(results) > 0:
        print("Statistics")
        for lates in range(len(results)):
            #print("Bus Route", busList[lates])
            print("Late Arrivals: ",str(results[0][lates]), "buses")
            print(f"Average number of minutes late for route ", str(results[1][lates]))
    else:
        print("all buses arrived on time")


print(printing(buses, days))


'''Task 3 – Checking specific days.
Extend the program as follows:
• Allow the user to input a specific day, for example Fri3, to be used for analysis of data.
• Find and display how many buses were late on this particular day.
• For each late bus, display the route label and how late the bus was on this particular dayyyyyy'''

