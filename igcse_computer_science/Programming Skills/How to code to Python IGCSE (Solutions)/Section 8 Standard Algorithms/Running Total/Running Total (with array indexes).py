# Standard Algorithm
# Running Total (Each item in a List using indexes)

total = 0

items = [12,3,54,35,23,56,34,3,77,9]

for count in range(len(items)):
    total = total + items[count]

print("The total =",total)