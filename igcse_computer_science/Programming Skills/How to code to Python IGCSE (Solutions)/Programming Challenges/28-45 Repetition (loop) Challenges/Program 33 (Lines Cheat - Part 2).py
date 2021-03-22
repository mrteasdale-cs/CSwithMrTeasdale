## Lines Cheat - Part 2
## Program 33
## With Comments

## The user is then asked to input a sentence (string) as before:

sentence = str(input("Which sentence would you like copied?"))

## The user is then asked to input the number of times the sentence:

times = int(input("How many times would you like this copied?"))

## The program then loops the number of times entered by the user
## by using the variable from earlier in the range().

for loop in range(times):
    print (sentence)

