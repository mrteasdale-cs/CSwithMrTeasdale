## Diving Scores
## Program 61
## With Comments

## The judges scores are entered as a single string.
print("Please enter the judges'scores:")
scores = str(input())

print("Please enter the difficulty rating")
rating = float(input())

## The seven scores are split, using the commas, into a 7 element list of strings.
separateScores = scores.split(",")

## Each element of the list is converted from a string to an integer
## using the int() function.
for eachScore in range(len(separateScores)):
    separateScores[eachScore] = int(separateScores[eachScore])

## The maximim value is identified and this is removed from the list.
## This is repeated for the minimum value.
## The loop ensures that two of each max and min are removed.
for loop in range(2):
    separateScores.remove(max(separateScores))
    separateScores.remove(min(separateScores))

## The remaining values in the list are totalled unsing sum() and
## multiplied by the dives difficulty rating.
finalScore = sum(separateScores) * rating

## Finally the required output is displayed.
print("The three remaining judges' scores are:")
for loop in range(len(separateScores)):
    print(separateScores[loop])

print("The diver's score is:",round(finalScore,1))


## Additional difficult challenge
## Validate the input of the original judges scores to ensure there are:
## - 7 scores
## - each score is separated by a comma
## Anything other than the above should be rejected and the user should
## be asked to re-enter the scores.
