# Section 3 - Repetition (Loop) Statements
# Example 34 – Input Validation

score = int(input("Please enter your score."))
while not(score >= 10 and score <= 20):
    print("Your score must be between 10 and 20 inclusive.")
    score = int(input("Please enter your score."))
