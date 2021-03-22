## Pailwater Darts Tournament
## Program 45
## With Comments

## Player one is stored as the winner for now.  This will change if
## one of player two's scores is the highest score.
winner = "Player one"

## This variable will store player one's highest score.
playerOne = 0

## Get the scores for player one and keep the largest score.
print("Please enter the scores for Player one")
for loop in range(3):
    score = int(input())

    ## A conditional loop is added to ensure the entered score is entered
    while not(score >= 0 and score <= 180):
        print("Invalid Score")
        score = int(input())

    ## An if statement checks to see if the score entered is larger than
    ## the currently stored value.
    if score > playerOne:
        playerOne = score



## The three scores for player two are entered and compared to player one's
## highest score.
print("Please enter the score for Player two")

for loop in range(3):
    score = int(input())

    ## A conditional loop is added to ensure the entered score is entered
    while not(score >= 0 and score <= 180):
        print("Invalid Score")
        score = int(input())

    ## If any of player two's scores are larger than player one's channge
    ## which player is stored as the winner.
    if score > playerOne:
        winner = "Player two"

## Display the result
print(winner,"scored the highest individual score.")
print(winner,"wins!!")

## Note that if none of player two's scores are the highest 'winner'
## still scores "Player one", the value it was given at the start of the
## program.