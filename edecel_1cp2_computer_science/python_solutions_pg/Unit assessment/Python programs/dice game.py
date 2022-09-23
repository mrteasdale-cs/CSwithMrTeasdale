# Players take turns to throw two dice.
# The player's score is the sum of the two dice, 
# but if they throw a double, this score is doubled 
# The score is added to the players total score after each throw.
# Each time a double is thrown, the player gets an extra turn
# If the player does not throw a double, the turn passes to the next player

#This code snippet shows one player's turn

import random

totalScore = 0
die1 = 0
die2 = 0
while die1 == die2:
    die1 = random.randint(1,6)
    print("die1 =", die1)
    die2 = random.randint(1,6)
    print("die2 =", die2)
    score = die1 + die2
    if die1 == die2:
       score = 2 * score
    print("Score for this throw =", score)
    totalScore = totalScore + score

print("Total score for this turn:", totalScore)

input("\nPress Enter to exit")
