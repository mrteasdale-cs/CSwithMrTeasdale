stringComplete = False
endString = ""
while not stringComplete:
    char = input("Enter next character: ")
    if char == "":
        stringComplete = True
    else:
        endString = endString + char

print(endString)
    
    
