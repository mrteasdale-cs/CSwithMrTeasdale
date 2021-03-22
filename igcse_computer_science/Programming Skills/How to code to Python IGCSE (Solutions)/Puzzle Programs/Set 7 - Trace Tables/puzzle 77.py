# Puzzle Program 77
text1 = "a"
text2 = "b"
text3 = ""
for loop in range(4):
    phrase1 = str(loop)+ text1
    phrase2 = text2 + str(loop)
    if loop <= 2:
        text3 = text3 + phrase1
    else:
        text3 = text3 + phrase2
print(text3)
