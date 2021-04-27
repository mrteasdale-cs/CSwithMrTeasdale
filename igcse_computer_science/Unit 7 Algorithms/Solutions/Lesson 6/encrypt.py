#What is this algorithm doing? write here


sentence = input("Please input a sentence: ")
#capitalise the string
sentence = sentence.upper()
key = int(input("Please enter offset between 1 and 10: "))

#list all the characters that can be encrypted
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encryptedSentence = ""

#what is happening below?
for letter in sentence:
    if letter in alphabet:
        num = alphabet.find(letter)
        num = (num + key)% 26
        encryptedSentence = encryptedSentence + alphabet[num]
    else:
        encryptedSentence = encryptedSentence + letter
print (encryptedSentence)


#Now what is happening below? write
sentence = encryptedSentence
decryptedSentence = ""
#Write here ?????
for letter in sentence:
    if letter in alphabet:
        num = alphabet.find(letter)
        num = num - key
        if num< 0:
            num = num + len(letters)
        decryptedSentence = decryptedSentence + alphabet[num]
    else:
        decryptedSentence = decryptedSentence + letter
print ("This sentence decrypted is: ", decryptedSentence)