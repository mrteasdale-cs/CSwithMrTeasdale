## Cricket Over - Part 3 (Alternative)
## Program 55
## With Comments

## Set up two 2D lists to store three for each team
scores1 = [[0] * 6 for main in range(3)]
scores2 = [[0] * 6 for main in range(3)]
game = "Y"

## Keep running the program while user keeps selecting y for
## another game.
while game.upper()=="Y":

    ## The total scores are reset to 0 inside the loop so that they will
    ## set back to 0 if the code repeats.
    team1Score = 0
    team2Score = 0

    ## The user is asked to enter the scores for the first three
    ## overs. Each score is added to a running total.
    for over in range(3):
        print("Please enter over "+str(over+1)+" for Team 1")
        for ball in range(6):
            scores1[over][ball] = int(input())
            team1Score = team1Score + scores1[over][ball]

    ## The user is asked to enter the scores for the second three
    ## overs. Again each score is added to a running total.
    for over in range(3):
        print("Please enter over "+str(over+1)+" for Team 2")
        for ball in range(6):
            scores2[over][ball] = int(input())
            team2Score = team2Score + scores2[over][ball]

    ## The total scores are displayed for both teamms.
    print("Score for Team 1's three overs:")
    print(team1Score)
    print("Score for Team 2's three overs:")
    print(team2Score)

    ## Ask the user if they wish to repeat all the above.  The conditional
    ## loop will repeat if the user enters y or Y.
    game = str(input("Do you wish to calculate the result of another game?"))