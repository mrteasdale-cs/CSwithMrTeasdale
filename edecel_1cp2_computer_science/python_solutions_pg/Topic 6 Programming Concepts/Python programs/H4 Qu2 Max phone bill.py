monthName =  ["January", "February", "March", "April", "May",
              "June", "July", "August", "September",
              "October", "November", "December"]
phoneBill =[0]*12
maxPhoneBill = 0
for m in range(0,12):
    print("Please input phone bill for month " + monthName[m])
    phoneBill[m] = float(input())
    if phoneBill[m] > maxPhoneBill:
        maxPhoneBill = phoneBill[m]
        maxMonth = monthName[m]
print("Maximum Phone Bill: " + maxMonth + " for " + str(maxPhoneBill))
