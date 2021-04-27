import time
#program to find average of n numbers

print ("Please enter a number between 2 and 20: ")
x = input()
n = int(x)
while n<2 or n>20:  
    print ("Please enter a number between 2 and 20: ")
    x = input()
    n = int(x)
#endwhile

#enter temperatures and calculate average
total = 0
for count in range (n):
    print ("Please enter temperature as an integer value: ")
    temperature = int(input())
    total = total + temperature
#next count
averageTemp = round(total/n,2)

print ("The average temperature is ",averageTemp)
time.sleep(10)
