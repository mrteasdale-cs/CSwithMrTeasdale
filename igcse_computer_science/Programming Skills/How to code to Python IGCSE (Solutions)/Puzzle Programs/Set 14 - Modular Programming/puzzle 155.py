# Puzzle Program 155
def textChanger1(word):
    wordLength = len(word)
    if wordLength <=2:
        return word
    elif wordLength>2 and wordLength<=6:
        temp1 = word[0:2]
        temp2 = word[len(word)-2:]
        word = temp2 + word + temp1
        return word
    else:
        temp1 = word[0:3]
        temp2 = word[len(word)-3:]
        print(temp1,temp2)
        word = temp2 + temp1
        return word

def textChanger2(word):
    if word.lower() == word:
        return word.upper()
    elif word.upper() == word:
        return word.lower()
    else:
        return "mixed"

def textChanger3(word):
    length = 5 * len(word)
    word = str(length-5) + word + str(length)
    return word

password = "hard"
password = textChanger3(textChanger2(textChanger1(password)))
print("Password is",password)
