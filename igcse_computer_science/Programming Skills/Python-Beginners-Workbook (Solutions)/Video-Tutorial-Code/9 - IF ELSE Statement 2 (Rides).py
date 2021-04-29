heightLimit = 120
ageLimit = 8

height = int(input("Enter your height in cm: "))
age = int(input("Enter your age in years: "))

if height >= heightLimit or age >= ageLimit:
    print("You may go on this ride.")
else:
    print("You cannot go on this ride.")
