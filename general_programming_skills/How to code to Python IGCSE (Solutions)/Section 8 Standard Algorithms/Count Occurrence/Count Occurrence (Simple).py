# Standard Algorithm
# Count Occurence (Simple)

numbers = [12,3,5,4,67,7,5,3,5,7,3,2,4,6,5,8,5,3,2,4,5,7,8,9,0,9,2,3,6,4,6,2,4,5,7,86,7,4,4]
occurrence = 0

target=int(input("State the value to count"))
for loop in range(len(numbers)):
    if numbers[loop] == target:
        occurrence = occurrence + 1

print(target,"appeared",occurrence,"times")