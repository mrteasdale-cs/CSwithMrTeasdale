userPass = [["dwilliams3","ivnduh39"],
            ["mamin2","xcvnmk18"],
            ["apatel","cvienms92"]]

validPass = False

while not validPass:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for userdetails in userPass:
        if userdetails[0] == username and userdetails[1] == password:
            print("Valid user")
            validPass = True

    if not validPass:
        print("Invalid user")
        

