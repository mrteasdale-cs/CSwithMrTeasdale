def convertDtoB(binNumber):
    place = 128
    denaryTotal = 0
    for digit in binNumber:
        denaryTotal = denaryTotal + (int(digit) * place)
        place = place / 2

    return denaryTotal

print(convertDtoB("10111100"))
print(convertDtoB("11111101"))
print(convertDtoB("00001101"))
print(convertDtoB("00011101"))

'''
number = 15
binary = bin(number)
print("{0:#b}".format(number))
print(int(binary,2))'''
