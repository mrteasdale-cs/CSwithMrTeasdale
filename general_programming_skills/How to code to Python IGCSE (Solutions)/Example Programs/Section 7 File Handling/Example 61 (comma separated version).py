# Section 7 – File Handling
# Example 61 – Reading from a Text File into Separate Lists
# Comma separated file

forename = []
surname = []
nickname = []

with open('Friends.csv','r') as pals:

	for each in pals.readlines():

		each = each[0:-1]
		temp = each.split(",")
		forename.append(temp[0])
		surname.append(temp[1])
		nickname.append(temp[2])

print(forename)
print(surname)
print(nickname)