import random

for i in range(0,5):
    hand1 = random.randint(1,3)
    hand2 = random.randint(1,3)
    player1 = ""
    player2 = ""
    if hand1 == 1:
        player1 = "Scissors"
    elif hand1 == 2:
        player1 = "Paper"
    elif hand1 == 3:
        player1 = "Stone"
        
    if hand2 == 1:
        player2 = "Scissors"
    elif hand2 == 2:
        player2 = "Paper"
    elif hand2 == 3:
        player2 = "Stone"


    print("Player 1: ", player1, ", Player2: ", player2)
    if player1 == player2:
        print("Draw")
    elif (player1 == "Scissors" and player2 == "Paper") or (player1 == "Stone" and player2 == "Scissors") or (player1 == "Paper" and player2 == "Stone"):
        print("Player 1 wins")
    else:
        print("Player 2 wins")
