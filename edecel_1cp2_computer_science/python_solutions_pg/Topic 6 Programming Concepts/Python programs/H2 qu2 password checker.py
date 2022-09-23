import random

customerPassword = "HC&dt2016"
numChars = len(customerPassword)
index1 = random.randint(0, numChars-1)
index2 = random.randint(0, numChars-1)
index3 = random.randint(0, numChars-1)

print("Please enter characters ")
print(index1+1)
print(index2+1)
print(index3+1)
print("Press enter after each character: ")
char1 = input("Enter character " + str(index1+1) + ": ")
char2 = input("Enter character " + str(index2+1) + ": ")
char3 = input("Enter character " + str(index3+1) + ": ")

match1 = char1 == customerPassword[index1]
match2 = char2 == customerPassword[index2]
match3 = char3 == customerPassword[index3]

if match1 and match2 and match3:
    print("Welcome")
else:
    print("Password incorrect")
    
input("Press ENTER to exit program ")
