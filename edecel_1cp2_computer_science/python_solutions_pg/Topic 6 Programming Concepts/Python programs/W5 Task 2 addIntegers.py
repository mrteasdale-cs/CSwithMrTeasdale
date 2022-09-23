def addIntegers(a, b):
    total = 0
    for i in range(a, b+1):
        total = total + i
    return total

#main program

print(addIntegers(5,10))
