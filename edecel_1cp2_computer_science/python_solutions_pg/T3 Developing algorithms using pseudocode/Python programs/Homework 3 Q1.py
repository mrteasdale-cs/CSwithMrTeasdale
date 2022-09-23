correctPassword = False
password = input("Please enter password: ")
if password == "NotAtHome!":
    print("Welcome")
    correctPassword = True
else:
    print("Wrong password")
