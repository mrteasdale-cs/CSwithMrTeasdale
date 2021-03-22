# Section 2 - Selection (if) statements
# Example 24 – Complex conditions (AND, OR)
# Efficient version

ticket = str(input("Do you wish to buy a ticket?"))
if ticket == "Y":
	print("Welcome to the ticket office.")
	age = int(input("Please enter your age"))
	if age >= 5 and age <= 17:
		print("Please purchase a junior ticket")
	if age > 17 and age < 65:
		print("Please purchase an adult ticket")
	if age >= 65:
		print("You are entitled to a senior ticket")
else:
	print("We are sorry to hear that.")
	print("Please return soon.")




