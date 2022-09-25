## The Most Vowels
## Program 24
## with comments

## The user is asked to enter two sentences.

sent1 = str(input("Enter sentence 1"))
sent2 = str(input("Enter sentence 2"))

## The count function is used to count the number of a,e,i,o,u
## characters in each sentence.

vowels1 = sent1.count("a") + sent1.count("e") + sent1.count("i") + sent1.count("o") + sent1.count("u")
vowels2 = sent2.count("a") + sent2.count("e") + sent2.count("i") + sent2.count("o") + sent2.count("u")

## The percentage of vowels in each sentence can be displayed.
## This is calculate as 100 / length of sentence * number of vowels
## The calculation is placed inside the round() function to ensure
## only 2 decimal places are displayed.

print ("The percentage of vowels in sentence 1 is:",round(100/len(sent1)*vowels1,2))
print ("The percentage of vowels in sentence 2 is:",round(100/len(sent2)*vowels2,2))

## The number of vowels in each sentence is displayed.

print("Sentence 1 has",vowels1,"vowels.")
print("Sentence 2 has",vowels2,"vowels.")

## An if statement is used to decide which sentence has the greatest
## number of vowels.

if vowels1 > vowels2:
    print("Sentence 1 has more vowels.")
if vowels1 < vowels2:
    print("Sentence 2 has more vowels.")

## Note that if statements can be often be written  several ways.