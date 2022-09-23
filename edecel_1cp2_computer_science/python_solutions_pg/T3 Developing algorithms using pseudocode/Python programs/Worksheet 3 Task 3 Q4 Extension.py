import random

def outcome(hand):
    if hand == 1:
        return "Scissors"
    elif hand == 2:
        return "Paper"
    elif hand == 3:
        return "Stone"

for i in range(0,5):
    hand1 = random.randint(1,3)
    hand2 = random.randint(1,3)
    player1 = ""
    player2 = ""

    player1 = outcome(hand1)
    player2 = outcome(hand2)


    print("Player 1: ", player1, ", Player2: ", player2)
    if player1 == player2:
        print("Draw")
    elif (player1 == "Scissors" and player2 == "Paper") or (player1 == "Stone" and player2 == "Scissors") or (player1 == "Paper" and player2 == "Stone"):
        print("Player 1 wins")
    else:
        print("Player 2 wins")
