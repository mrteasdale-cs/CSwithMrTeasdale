#Worksheet task 2 Rainfall 1

Months =  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
rainfall =[0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,12):
    print("Please input rainfall for month ",Months[i])
    rainfall[i] = input()
print ("Thanks")
for i in range(0,12):
    print(Months[i], rainfall[i])

#Worksheet task 2 Rainfall 2

Months =  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
rainfall  =[0,0,0,0,0,0,0,0,0,0,0,0]
annualRainfall = 0
for i in range(0,12):
    print("Please input rainfall  for month ",Months[i])
    rainfall [i] = int(input())
    annualRainfall = annualRainfall + rainfall[i]
print ("Thanks")
averageRainfall = annualRainfall/12
roundedAverage = round(annualRainfall/12,1)
monthsAboveAverage = 0
for i in range(0,12):
    if rainfall[i] > averageRainfall:
        monthsAboveAverage +=1   #add 1 to monthlyAverage
    print(Months[i], rainfall[i])
print("Annual rainfall = ", annualRainfall)
print ("Average monthly rainfall", roundedAverage)
print("\nNumber of months above average rainfall: ", monthsAboveAverage)  


####################
#Homework Python Code

#Q1 program to measure the time it takes a user to type a sentence
import time

sentence = input("Enter a sentence to be timed on: ")
n=len(sentence)
print("Number of characters",n)
firstChar = sentence[0]
print ("First character is ", firstChar)
errorFlag = 0
print("Start typing! Press Enter when finished ")
startTime = time.perf_counter()


mySentence = input()
finishTime = time.perf_counter()
print ("Sentence to type: ", sentence)
print ("You typed: ", mySentence)
       
if mySentence!=sentence:
    errorFlag = 1

totalTime = finishTime-startTime
startTime = round(startTime,3)
finishTime = round(finishTime,3)
print ("Start time, finish time ", startTime, finishTime)
totalTime = round(totalTime,3)
if errorFlag:
    print ("You made one or more errors")
else:
    print ("Total time taken ",totalTime, "seconds")
finish = input("Press Enter to end")


# Phone Bill task

MonthName =  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
PhoneBill =[0,0,0,0,0,0,0,0,0,0,0,0]
MaxPhoneBill = 0

for i in range(0,12):
    print("Please input phone bill for month ",MonthName[i])
    PhoneBill[i] = float(input())
    if PhoneBill[i]>MaxPhoneBill:
        MaxPhoneBill = PhoneBill[i]
        MaxMonth = MonthName[i]

print("Maximum Phone Bill: ",MaxMonth, MaxPhoneBill)        

