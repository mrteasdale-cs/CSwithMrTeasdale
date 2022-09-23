import random

running = True
choices = ['rock', 'paper', 'scissors']
print('''Rock, Paper, Scissors Game
==========================''')


def run_Game():
    userchoice = str(input("Enter your move: s, r, p"))
    while userchoice != "rock" or userchoice != "scissors" or userchoice != "paper":
        userchoice = str(input("Enter your move: s, r, p"))

    randindex = random.randint(0, 2)
    randompick = choices[randindex]
    result = game_Round(userchoice, randompick)
    return userchoice, result


def game_Round(userchoice, aichoice):
        if userchoice == aichoice:
            return 0, aichoice
        elif (userchoice == "rock" and aichoice == "scissors") \
                or (userchoice == "scissors" and aichoice == "paper") \
                or userchoice == "paper" and aichoice == "rock":
            return 1, aichoice
        else:
            return -1, aichoice


def exit():
    stop = input("Press any key to continue or 0 to quit")
    if stop == 0:
        return False


while running:
    result = run_Game()
    user = result[0]
    ai = result[1][1]
    if result[1][0] == 1:
        print(f"you win! {user} beats {ai}!".format(user=user, ai=ai))
    elif result[1][0] == -1:
        print(f"LOSER! - {ai} beats {user}!".format(user=user, ai=ai))
    elif result[1][0] == 0:
        print(f"draw! {user} draws with {ai}!".format(user=user, ai=ai))
    exit()
