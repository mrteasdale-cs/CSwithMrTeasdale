# Standard Algorithm
# Find Maximum (in a List)

numbers = [12,3,5,4,67,7,5,3,5,7,3,2,4,6,5,8,86,4,4,9]
maximum = numbers[0]

for counter in range(1,len(numbers)):
    if numbers[counter] > maximum:
        maximum = numbers[counter]

print("Maximum value is:",maximum)