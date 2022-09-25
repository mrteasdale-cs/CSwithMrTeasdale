# Section 4 – Storing Multiple Values using Lists
# Example 45 - split( )

sentence = "Demonstrate the split function."
words = [""]
words = sentence.split(" ")
for loop in range(len(words)):
	print(words[loop])