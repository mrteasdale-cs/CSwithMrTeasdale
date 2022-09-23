print("This program prints selected numbers in a given range")
print("which are not divisible by 5 or 7")
anotherGo = "Y"
while anotherGo == "Y":
    lowNumber = int(input("Please enter first number in your chosen range: "))
    highNumber = int(input("Please enter last number in your chosen range: "))
    totalNum = 0
    for i in range(lowNumber, highNumber + 1):
        if i % 5 != 0 and i % 7 != 0:
            print(i)
            totalNum = totalNum + 1
            
    print(str(totalNum) + " numbers are not divisible by 5 or 7")
   
    answer = input("Another go? (Y or N)")
    anotherGo = answer.upper()

