# Puzzle Program 42
statement = "When Mr. Bilbo Baggins of Bag End announced"
letter1position = statement.count("a")
letter2position = statement.count("e")
letter3position = statement.count("i")
letter4position = statement.count("o")
letter1 = statement[letter1position-1:letter1position]
letter2 = statement[letter2position-1:letter2position+2]
letter3 = statement[letter3position-1:letter3position]
letter4 = statement[letter4position+1:letter4position+3]
password = letter2 + letter4 + letter3 + letter1
print (password)