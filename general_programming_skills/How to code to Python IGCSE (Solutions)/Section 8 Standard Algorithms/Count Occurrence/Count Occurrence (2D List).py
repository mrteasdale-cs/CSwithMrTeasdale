# Standard Algorithm
# Count Occurence (2D List)

numbers = [[12,3,5,4],[67,7,5,3],[5,7,3,2],[4,6,5,8],[5,3,2,4],[5,7,8,9],[0,9,2,3],[6,4,6,2],[4,5,7,86],[7,4,4,6]]
occurrence = 0

target=int(input("State the value to count"))
for outerLoop in range(len(numbers)):
    for innerLoop in range(len(numbers[outerLoop])):
        if numbers[outerLoop][innerLoop] == target:
            occurrence = occurrence + 1

print(target,"appeared",occurrence,"times")