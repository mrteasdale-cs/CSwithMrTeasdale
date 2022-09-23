import random
die1 = random.randint(1,6)
die2 = random.randint(1,6)

score = die1 + die2
if die1 == die2:
    score = score * 2
if die1 == die2 == 6:
    score = 0

print(die1)
print(die2)
print(score)
