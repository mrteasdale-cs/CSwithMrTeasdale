import random
running = True
choices = ['rock', 'paper', 'scissors']

def gameRound(userchoice, aichoice):
    if userchoice == aichoice:
        return 0, aichoice
    elif (userchoice == "rock" and aichoice == "scissors") \
            or (userchoice == "scissors" and aichoice == "paper") \
            or userchoice == "paper" and aichoice == "rock":
        return 1, aichoice
    else:
        return -1, aichoice

def runGame():
    userchoice = str(input("Enter your move: "))
    randindex = random.randint(0,2)
    randompick = choices[randindex]
    result = gameRound(userchoice, randompick)
    return userchoice, result

def exit():
    stop = input("Press any key to continue or 0 to quit")
    if stop == 0:
        return False

while running:
    result = runGame()
    user = result[0]
    ai = result[1][1]
    if result[1][0] == 1:
        print(f"you win! {user} beats {ai}!".format(user=user,ai=ai))
    elif result[1][0] == -1:
        print(f"you lose! you are poop - {ai} beats {user}!".format(user=user,ai=ai))
    elif result[1][0] == 0:
        print(f"draw! {user} is the same {ai}!".format(user=user,ai=ai))
    exit()





