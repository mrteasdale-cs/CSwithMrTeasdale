# Section 2 - Selection (if) statements
# Example 25 - Else if (elif)

age = int(input("Please enter your age"))
if age >= 0 and age < 5:
	print("Sorry, You are too young to attend")
elif age >= 5 and age < 18:
	print("Please purchase a junior ticket")
elif age >= 18 and age < 65:
	print("Please purchase an adult ticket")
elif age >= 65:
	print("You are entitled to a senior ticket")
else:
    print("Invalid age")




