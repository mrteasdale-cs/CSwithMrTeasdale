password = "EpCg3E4("
validPassword = False

while not validPassword:
    userPass = input("Enter the password: ")
    if userPass == password:
        print("Valid password")
        validPassword = True
    else:
        print("Invalid password")

