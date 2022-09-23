passwordOK = False
count = 0
while count < 3 and not passwordOK:
    password = input("Please enter password: ")
    if password == "AXcd35" :
        passwordOK = True
    else:
        print("Password incorrect")
        count = count + 1
if passwordOK:
    print("Welcome back")
else:
    print("contact administrator")
    
input("\nPress Enter to exit")

