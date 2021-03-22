## No more presents
## Program 41
## With Comments

## As a running total of the present cost will be stored it must
## first be initialised to 0.

totalCost = 0

## The program should loop until the total cost of the presents is at least 200.

print("Please enter the price of each present:")
while totalCost <= 200:
    cost = int(input())
    totalCost = totalCost + cost

## After the program exits the loop the value of the last present is displayed
## in a message.

print("Limit Exceeded")
print("You can't include the £"+str(cost),"present.")


## Note - the challenge doesn't require you to make sure the correct total cost
## is stored.  Another line, after the loop, taking the cost of the last present
## back off the total would solve that issue.
## totalCost = totalCost - cost
