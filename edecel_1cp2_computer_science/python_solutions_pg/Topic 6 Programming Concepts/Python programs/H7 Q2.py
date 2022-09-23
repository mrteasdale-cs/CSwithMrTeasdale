validWeight = False
validLength = False
validTerms = False

weight = 0
length = 0
terms = False

while not validWeight:
    weight = int(input("Enter weight of parcel: "))
    if weight >= 1 and weight <= 10:
        validWeight = True
    else:
        print("Invalid input")

while not validLength:
    length = int(input("Enter longest length of parcel: "))
    if length >= 1 and length <= 100:
        validLength = True
    else:
        print("Invalid input")

while not validTerms:
    terms = input("Enter 'y' if you accept the terms and conditions: ")
    if terms == "y":
        validTerms = True
    else:
        print("Invalid input")

print("Package accepted")
