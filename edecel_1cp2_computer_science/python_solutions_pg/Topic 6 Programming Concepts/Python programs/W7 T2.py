username = ""
validUsername = False
while not validUsername:
    username = input("Enter username: ")
    if username.isalpha():
        validUsername = True
        print("Valid username")
    else:
        print("Invalid username")

validID = False
ID = ""
while not validID:
    ID = input("Enter ID: ")
    if ID[0] == 'I' and ID[1] == 'D':
        print("Valid ID")
        validID = True
    else:
        print("Invalid ID")


validRoom = False
roomNum = ""
while not validRoom:
    roomNum = input("Enter room number: ")
    if roomNum[0].isalpha() and roomNum[0].isupper() and roomNum[1].isdigit() and roomNum[2].isdigit and len(roomNum) == 3:
        print("Valid room")
        validRoom = True
    else:
        print("Invalid room")
    
    
    
