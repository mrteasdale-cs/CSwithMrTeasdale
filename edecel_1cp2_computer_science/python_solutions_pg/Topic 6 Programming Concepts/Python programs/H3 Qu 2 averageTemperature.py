print("Please enter number of temperatures (between 5 and 20): ")
validNumber = False
while not validNumber:
    numTemp = int(input())
    if numTemp >= 5 and numTemp <= 20:
        validNumber = True
    else:
        print("Please enter a number between 5 and 20: ")


#enter temperatures and calculate average
total = 0
for i in range(numTemp):
    temp = int(input("Please enter temperature as an integer value: "))
    total = total + temp

averageTemp = total/numTemp
print(averageTemp)
    
