## Go Winner
## Program 21
## with comments

## The user is asked to input the scores for each player:

black = int(input("What is Black's score?"))
white = int(input("What is White's score?"))

## The problem states that white gets an additional 6.5 points
## at the end of the game.

white = white + 6.5

## Each score is then displayed.
print("After 6.5 is added the score is:")
print("Black -",black)
print("White -",white)

## The program compares the two player's scores and displays a
## different message depending on the result.

if black > white:
    print ("Black is the winner.")
if white > black:
    print ("White is the winner.")


## Note that the above if statements could be combined into a
## single more efficient solution.

##if black > white:
##    print ("Black is the winner.")
##else:
##    print ("White is the winner.")