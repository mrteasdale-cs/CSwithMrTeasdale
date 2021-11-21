# Calculate the milk yield for a herd of cows
# Author: Mr Teasdale
# IGCSE CS Pre-Release Task
herdSize=2
cowId=["111","222"]
totalWeeklyYield=[28.9,30,17,20.4,23,29,40,36,11,32,27,15,5,24]
cowsDailyTotal=[]
session1=0
session2=0
count=0
count2=0
totalMilkVol=0
avgMilk=0

herdSize = int(input("Enter the amount of cows in herd"))
acceptId = False

for cow in range(0,herdSize):
  acceptId = False
  cowid = input("Enter cow ID: ")

  while len(cowid) < 3:
    print("ID too short: ")
    cowid=input("Enter ID again: ")

  while acceptId != True:
    if cowid not in cowId:
      acceptId = True
      cowId.append(cowid)
      print("ID entered!")
    else:
      acceptID = False
      cowid = input("Already an ID in the list. Entera new cow ID: ")

for day in range(0,2):
  #day=input("Enter a day: ")
  for i in range(herdSize):

    print("enter the milk produced in session 1 for ",cowId[i])
    session1=float(input())
    round(session1,2)
    print("enter the milk produced in session 2 for ",cowId[i])
    session2=float(input())
    round(session2,2)
    totalDay=session1+session2
    totalWeeklyYield.append(totalDay)
    count += 1

  for x in range(herdSize):
    totalMilkVol = totalMilkVol+totalWeeklyYield[count2]
    count2 += 1

avgMilk = totalMilkVol / len(totalWeeklyYield)

print("Cow IDs: ",cowId)
print("\nmilk yields: ",totalWeeklyYield)
print("\nTotal milk produced this week: ",round(totalMilkVol,1))
print("\nAverage milk produced this week: ",round(avgMilk,1))