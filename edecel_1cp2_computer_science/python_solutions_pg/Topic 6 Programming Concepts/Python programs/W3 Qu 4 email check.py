validEmail = False

while not validEmail:
    email = input("Enter your email address: ")
    for letter in email:
        if letter == "@":
            validEmail = True

        
