import random
words = 0
wordlist = []
while words != 10:
    lines = open('words.txt').read().splitlines()
    myline = random.choice(lines)
    wordlist.append(myline)
    words = words+1
print("\n".join(wordlist))

input("\nfinished. press enter...")
