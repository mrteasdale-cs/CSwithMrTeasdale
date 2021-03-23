# Section 4 – Storing Multiple Values using Lists
# Example 46 - index()
# Index with sub-string

sentence = "It's time for the human race to enter the solar system."
firstHalf = ""
secondHalf = ""

firstHalf = sentence[ :sentence.index("to")]
secondHalf = sentence[sentence.index("to"): ]

print(firstHalf)
print(secondHalf)

