game = "Minecraft"
guess = input("Guess what my favourite video game is: ")

while guess != game:
    guess = input("Incorrect - try again! \n \nGuess what my favourite video game is: ")

print("Congratulations - you guessed my favourite video game!")