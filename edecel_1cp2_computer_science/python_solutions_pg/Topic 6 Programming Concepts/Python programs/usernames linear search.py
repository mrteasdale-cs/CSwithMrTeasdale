usernames = ["psmith", "ltorvalds", "pwatts", "sjones",
             "mpatel", "bwright", "mgreen",
             "dthomas", "nwhite", "fdavies"]

search = input("Type in username: ")

for i in range(len(usernames)):
    if usernames[i] == search:
        print("Name found")



