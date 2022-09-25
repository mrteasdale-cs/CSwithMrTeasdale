#reading from a file
file = open("words.txt", 'r')

for word in file:
    print(word)

#writing to a new file
file = open("newwords.txt", 'w')

for n in range(1,5):
    word = input("Write a word")
    word+=" "
    file.write(word)


file.close()