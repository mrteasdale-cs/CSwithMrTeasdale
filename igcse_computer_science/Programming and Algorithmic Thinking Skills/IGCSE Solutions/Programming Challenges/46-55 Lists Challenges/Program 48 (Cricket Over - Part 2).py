## Cricket Over - Part 2
## Program 48
## With Comments

total = 0

## A list of 6 elements, initialised to 0, is created to store the balls.
balls = [0]*6

print("Please enter the score for each ball.")

for loop in range(6):
    balls[loop] = int(input())   ## The input is changed to store each ball in the list
    total = total + balls[loop]

print("This over’s score was:",total)
print("With each ball scoring:")

## A second loop is used to display the ball scores.
for loop in range(6):
    print(balls[loop])