import time

sentence = "The quick brown fox jumped over the lazy dog"
n = len(sentence)
print("Sentence to type: ", sentence)

mistakeMade = False
print("Press Enter when you're ready to start typing! Press Enter when finished")
ready = input()
print("Go!")

startTime = time.perf_counter()

mySentence = input()

finishTime = time.perf_counter()
totalTime = finishTime - startTime

if mySentence != sentence:
    mistakeMade = True

if mistakeMade:
    print("You made one or more errors")
else:
    print("Total time taken ", totalTime, "seconds")
    print("Your sentence contained ", n, "characters")

input("Press Enter to exit program")
