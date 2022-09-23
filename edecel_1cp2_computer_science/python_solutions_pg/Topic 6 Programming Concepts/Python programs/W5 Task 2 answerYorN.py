def answerYorN():
    validAnswer = False
    while not validAnswer:
        response = input("Please enter y or n: ")
        response = response.lower()
        if response == "y" or response == "n":
            validAnswer = True
    return response

#main program

answer = answerYorN()
print(answer)

