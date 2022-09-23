over100 = 0
score = 0
while score != -1:
    score = int(input("Please enter the next score, -1 to end: "))
    if score > 100:
        over100 = over100 + 1
print(over100)
