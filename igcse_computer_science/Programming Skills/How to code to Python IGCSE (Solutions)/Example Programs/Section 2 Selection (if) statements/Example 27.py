# Section 2 - Selection (if) statements
# Example 27 – Building more complex if statements

score = int(input("Please enter your score."))
score2 = int(input("Please enter your score."))
score3 = int(input("Please enter your score."))
if ((score >= 23 and score <=33) or (score2 >= 45 and score2 <= 55)) and score3 != 0:
	print("Well done. That’s the correct combination of scores.")
else:
    print("You did not achieve the correct combination of scores.")