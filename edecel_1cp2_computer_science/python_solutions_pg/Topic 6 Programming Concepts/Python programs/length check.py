validNameLength = False
name = ""
while not validNameLength:
    name = input("Enter your name: ")
    if len(name) >= 8:
        validNameLength = True
