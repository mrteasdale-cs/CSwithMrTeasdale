## Password Generator
## Program 67
## With comments

import random

## Note that rather than retaining any of the text scrambling functions,
## as the challenge suggests, five new ones have been written as examples.

## A function to reverse any string that is passed into it.
## This loops backwards through each letter of the word.  Each letter
## is concatenated onto a new string.
def textChanger1(word):
    newWord = ""
    for chars in range(len(word),0,-1):
        newWord =  newWord + word[chars-1:chars]
    return newWord

## A function to randomly swap the case of some letters.
## Generate a random number which will be used to identify one letter
## in the word.  If this letter is a lower case letter, split the word
## apart using sub-string and put it back together while changing the
## random letter to upper case.  If already upper case change to lower.
def textChanger2(word):
    numberOfChanges = int(len(word)/2)
    for changes in range(numberOfChanges):
        char = random.randint(0,len(word)-1)
        if word[char:char+1].lower() == word[char:char+1]:
            word = word[:char] + word[char:char+1].upper() + word[char+1:]
        else:
            word = word[:char] + word[char:char+1].lower() + word[char+1:]
    return word

## A function to generate random numbers to add to the password.
## The numbers are rounded, converted to strings and concatenated
## onto the front and back of the user's word.
def textChanger3(word):
    length = random.randint(0,len(word)*10) /2
    length2 = random.randint(0,len(word)*7) /4
    word = str(round(length,2)) + word + str(round(length2,1))
    return word

## A function to combine two randomly chopped up words.
## Ask for another word.  Identify a random position in the users
## original word and the new word.  Chop the two words in half using
## sub-string (and the random positions) then concatenate the four
## half words together.
def textChanger4(word):
    otherWord = str(input("Please enter a second short word"))
    position1 = random.randint(0,len(word)-1)
    position2 = random.randint(0,len(otherWord)-1)
    word = word[:position1] + otherWord[position2:] + word[position1:] +  otherWord[:position2]
    return word

## A function to shuffle the letters in a word.
## Generate a random number, copy the letter at that location in#
## the word.  Rebuild the word, using sub-string, cutting that
## letter out and concatenating it to the end of the word.
def textChanger5(word):
    for chars in range(10):
        position = random.randint(0,len(word)-1)
        removed = word[position]
        word = word[:position] + word[position+1:] + removed
    return word

## MAIN PROGRAM
startingText = str(input("Please enter your word:"))
combination = random.randint(1,3)

## Call the functions in a different order depending on the random
## number generated above.
if combination == 1:
    password = textChanger1(startingText)
    password = textChanger3(password)
    password = textChanger5(password)
elif combination == 2:
    password = textChanger2(startingText)
    password = textChanger4(password)
    password = textChanger1(password)
else:
    password = textChanger4(startingText)
    password = textChanger3(password)
    password = textChanger2(password)
## Display the final password.
print("Password is",password)
