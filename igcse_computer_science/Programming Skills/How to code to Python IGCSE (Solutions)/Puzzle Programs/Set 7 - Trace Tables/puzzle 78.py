# Puzzle Program 78
text1 = "this"
text2 = "is"
text3 = "hard"
words = ""
number = 0
for diamond in range(len(text2),len(text3)):
    words = words + text1 + text2
    number = number + words.count("s")
    words = words[2:5] + text3
    number = diamond + number + words.count("h")
print(number)
