## Cricket Over - Part 3
## Program 55
## With Comments

## Set up a 2D list to store the six overs (three for each team)
scores = [[0] * 6 for main in range(6)]
game = "Y"

## Keep running the program while user keeps selecting y for
## another game.
while game.upper()=="Y":

    ## The total scores are reset to 0 inside the loop so that they will
    ## set back to 0 if the code repeats.
    team1Score = 0
    team2Score = 0

    ## The user is asked to enter the scores for the first three
    ## overs (0 to 2 of the main index of the 2D list)
    for over in range(3):
        print("Please enter over "+str(over+1)+" for Team 1")
        for ball in range(6):
            scores[over][ball] = int(input())

    ## The user is asked to enter the scores for the second three
    ## overs (3 to 5 of the main index of the 2D list)
    for over in range(3,6):
        print("Please enter over "+str(over-2)+" for Team 2")
        for ball in range(6):
            scores[over][ball] = int(input())

    ## The total scores are displayed for team 1.  A running total is
    ## used to add up the total for the first half of the 2D list.
    print("Score for Team 1's three overs:")
    for over in range(3):
        for ball in range(6):
            team1Score = team1Score + scores[over][ball]
    print(team1Score)

    ## Do the same for the second half of the 2D list.
    print("Score for Team 2's three overs:")
    for over in range(3,6):
        for ball in range(6):
            team2Score = team2Score + scores[over][ball]
    print(team2Score)

    ## Ask the user if they wish to repeat all the above.  The conditional
    ## loop will repeat if the user enters y or Y.
    game = str(input("Do you wish to calculate the result of another game?"))


## Note 1 - The program could have been designed with two 2D lists rather than
## using the two halves of one lst to store the scores.
## Note 2 - The running totals for each teams scores could have been calculated
## in the same loops where the input of scores happens.
## The above has been saved as Program 55(Cricket Over - Part 3 alternative).py