print("This program prints selected numbers in in given range. ")
anotherGo = "Yes"
while anotherGo == "Yes":
    lowNumber = int(input("Enter low number: "))
    highNumber = int(input("Enter high number: "))
    x = 0
    for i in range(lowNumber, highNumber+1):
        if i % 5 != 0 and i % 7 != 0:
            print(i)
            x = x + 1
    print(x,"numbers")
    anotherGo = input("Enter 'Yes' for another go: ")
