# Standard Algorithm
# Running Total

total = 0
items = int(input("Enter number of items"))

for count in range(items):
    temp = int(input("Enter value "+str(count+1)))
    total = total + temp

print("The total =",total)