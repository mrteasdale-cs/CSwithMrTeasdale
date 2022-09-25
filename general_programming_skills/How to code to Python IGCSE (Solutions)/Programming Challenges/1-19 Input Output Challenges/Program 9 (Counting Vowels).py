## Counting Vowels
## Program 9
## with comments

sentence = str(input("Please enter a sentence of your choice."))
sentence = sentence.lower()

vowelsa = sentence.count("a")
vowelse = sentence.count("e")
vowelsi = sentence.count("i")
vowelso = sentence.count("o")
vowelsu = sentence.count("u")

print ("Your sentence contained the following:")
print("a =",vowelsa)
print("e =",vowelse)
print("i =",vowelsi)
print("o =",vowelso)
print("u =",vowelsu)

total = vowelsa + vowelse + vowelsi + vowelso + vowelsu

print ("This is a total of",total,"vowels.")