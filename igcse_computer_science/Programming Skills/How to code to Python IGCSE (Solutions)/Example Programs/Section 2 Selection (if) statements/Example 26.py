# Section 2 - Selection (if) statements
# Example 26 - The ‘not’ operator

score = int(input("Please enter your score."))
if not(score == 76 or score == 58):
    print("You did not hit the target scores.")
else:
    print("Well done, target score achieved.")