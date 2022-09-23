consent = False

while not consent:
    response = input("Do you agree with the terms and conditions? ")
    if response == 'y':
        consent = True
        print("Thank you for your consent")
    else:
        print("Sorry, you must consent to use the program")
