moreTemps = True

while moreTemps:
    centigrade = float(input("Enter temp in centigrade"))
    farenheit = centigrade * (9 / 5) + 32 #calculates farenheit

    print(farenheit)

    #exit the loop if the user enters n
    enterMoreTemps = input("Enter more temps? ")
    if enterMoreTemps == 'n':
        moreTemps = False
        
