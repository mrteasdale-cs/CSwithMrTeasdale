import random
anotherGo = True
score = 0
while anotherGo:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print("die 1 =", die1, ", die 2 =", die2)
    if die1 == die2:
        anotherGo = False
        score = 0
        print("Score = ", score)
    else:
        score = score + die1 + die2
        print("Score = ",score)
        if (input("Another go? (y or n): ") == "n"):
            anotherGo = False

print("Final Score = ",score)

input()