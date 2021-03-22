# Puzzle Program 55
value = float(input("Please enter the value of your item"))
weight = float(input("Please enter the weight of your item in kilograms"))
if value <= 0:
	print("Invalid value")
	postage = 0.0
if weight >= 0 and weight < 2:
	if value > 0 and value < 50:
		postage = 1.5
	if value >= 50 and value < 150:
		postage = 2.75
	if value >= 150:
		postage = 5.5
elif weight >= 2 and weight < 10:
	if value > 0 and value < 50:
		postage = 2.5
	if value >= 50 and value < 150:
		postage = 4.4
	if value >= 150:
		postage = 8.35
elif weight >= 10 and weight < 25:
	if value > 0 and value < 50:
		postage = 7.55
	if value >= 50 and value < 150:
		postage = 12.3
	if value >= 150:
		postage = 15.0
else:
	postage = 25.0
print(postage)


