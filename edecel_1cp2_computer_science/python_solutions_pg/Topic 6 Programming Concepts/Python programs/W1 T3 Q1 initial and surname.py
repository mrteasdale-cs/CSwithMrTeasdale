firstName = input("Enter your first name: ")
surname = input("Enter your surname: ")
initial = firstName[0]			#find first letter of firstName
initial = initial.upper()		#convert to uppercase
surnameStart = surname[0]		#find first letter of surname
surnameStart = surnameStart.upper()	#convert to uppercase
surname = surname.lower()		#convert surname to lowercase
length = len(surname)			#length of surname
surname = surnameStart + surname[1:]
#concatenate the first letter of surname with remaining letters
fullName = initial + " " + surname	#concatenate the output
print(fullName)
