# Section 4 – Storing Multiple Values using Lists
# Example 45 - split( )
# Split using a string

sentence = "Even if you’re on the right track, you’ll get run over if you just sit there."
words = [""]
words = sentence.split("you")
for loop in range(len(words)):
	print(words[loop])