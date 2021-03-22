# Puzzle Program 41
sentenceOne = "The to boys learned to new skills"
sentenceTwo = sentenceOne.replace("to","two")
sentenceThree = sentenceTwo.replace("boys","girls")
totalLetterW = sentenceOne.count("w")+sentenceTwo.count("w")+sentenceThree.count("w")
totalLetterB = sentenceOne.count("b")+sentenceTwo.count("b")+sentenceThree.count("b")
print(totalLetterW+totalLetterB)