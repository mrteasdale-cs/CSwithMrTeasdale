# Puzzle Program 54
age = int(input("Please enter an age"))
if age < 0 or age > 120:
	print("Age not valid")
else:
	print("Valid age")
	if age >= 3 and age <= 18:
		print("School age")
	if age >= 16:
		print("Working age")
	if age >= 60:
		print("Retirement age")
	if age >= 67:
		print("Pension age")

