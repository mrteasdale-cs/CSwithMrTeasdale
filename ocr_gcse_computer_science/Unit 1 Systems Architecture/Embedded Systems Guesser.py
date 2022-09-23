'''Harder: Create a Python program that displays either the name of a device or a characteristic of an embedded system,
the user has to identify if it is an embedded system or not.'''
# Author: Mr Teasdale (M.Ed)
import random

devices = [["Shower", "n"], ["Traffic Lights", "y"], ["Digital Watch", "y"],
           ["Washing Machine", "y"], ["Smartphone", "n"], ["Macbook", "n"]]
characteristics = [["Usually used for very specialised tasks.", "y"], ["Can do multiple tasks at once.", "n"],
                   ["Has a single microprocessor", "y"], ["Contains and Operating System", "n"]]


def run():
    play = "y"
    score = 0
    print("Embedded System Guesser.\nCan you guess if its an embedded system or not?\n")

    while play != "n":

        print('''Press 1 or 2:
            1. Device Name
            2. Characteristic
            ''')
        choice = int(input())
        flag = True

        while flag == True:
            if choice == 1:
                random_no = random.randint(0, len(devices) - 1)
                thing = devices[random_no][0]
                print("\nDevice: ", thing, "\n")
                guess = str(input("Type y or n\n\n"))

                if devices[random_no][1] == guess:
                    print("Correct, well done.")
                    score += 1
                else:
                    print("Incorrect, better luck next time")
                flag = False
            elif choice == 2:
                random_no = random.randint(0, len(characteristics) - 1)
                thing = characteristics[random_no][0]
                print("\n", thing, "\n")
                guess = str(input("Type y or n\n\n"))

                if characteristics[random_no][1] == guess:
                    print("Correct, well done.")
                    score += 1
                else:
                    print("Incorrect, better luck next time")
                flag = False
            else:
                print("Error. Choose again")

        play = input("Play again? type y\n")
    print("You scored:", score, "point(s)")


run()