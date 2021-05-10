'''Task 1 – Setting up the data storage.
Using arrays set up a system to enable data for each bus route to be entered covering each day of a four-week period. It must be
possible to enter the data supplied or your own set of data, using suitable prompts as necessary.'''
import random
from array import *
'''Task 1 – Setting up the data storage.
Using arrays set up a system to enable data for each bus route to be entered covering each day of a
four-week period. It must be possible to enter the data supplied or your own set of data, using suitable
prompts as necessary.'''

def setup_storage():
    bus_a = []
    bus_b = []
    bus_c = []
    bus_d = []
    bus_e = []
    bus_f = []
    buses = ["A","B","C","D","E","F"]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

    for a in range(0,19):
        for aday in range(0, 5):
            minutes = int(input(f"Enter the minutes for bus {buses[0]} on day {days[aday]}{aday+1}".format(buses[0],days)))
            bus_a.append(minutes)


    for aday in range(0, 5):
        minutes = int(input(f"Enter the minutes for bus {buses[1]} on day {days[aday]}{aday +1}".format(buses[1], days)))
        bus_a.append(minutes)

    return bus_a

'''Task 2 – Working out the statistics.
Extend your program so that the following statistics for the four-week period may be calculated and
output:
• the number of late arrivals for each bus route
• the average number of minutes late for each bus route
• the bus route with the highest number of days on which it was late
• the average number of minutes late for each bus route, using only data from days on which it was
late. All the results should be displayed with appropriate annotation.'''
# Statistics
def getStats(bus_a):
    countA = 0
    totalA = 0
    for i in range(0,19):
        if bus_a[i] < 0:
            countA += 1
            totalA = bus_a[i] + totalA
    print(countA, totalA)

'''def printing(busList, dayList):
    results = getStats()
    print(results)
    if len(results) > 0:
        print("Statistics")
        for lates in range(len(results)):
            #print("Bus Route", busList[lates])
            print("Late Arrivals: ",str(results[0][lates]), "buses")
            print(f"Average number of minutes late for route ", str(results[1][lates]))
    else:
        print("all buses arrived on time")'''

buses = setup_storage()
getStats(buses)
#printing(buses, days)


'''Task 3 – Checking specific days.
Extend the program as follows:
• Allow the user to input a specific day, for example Fri3, to be used for analysis of data.
• Find and display how many buses were late on this particular day.
• For each late bus, display the route label and how late the bus was on this particular dayyyyyy'''