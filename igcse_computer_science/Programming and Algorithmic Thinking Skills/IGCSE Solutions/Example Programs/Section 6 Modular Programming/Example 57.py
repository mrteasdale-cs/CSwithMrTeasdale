# Section 6 – Modular Programming
# Example 57 – A Function Returning a Value

def interestCalculator(loan,period,interest):
	total = loan
	for years in range(period):
		total = total * (1+interest/100)
	return total

# Main Program
amount = int(input("Enter borrowing amount"))
years = int(input("Enter length of loan (years)"))
interest = float(input("Enter rate of interest"))
repayment = interestCalculator(amount,years,interest)
print("Repayment amount =",round(repayment,2))