def ftintom(feet, inch=0.0):
    return feet*0.3048+inch*0.0254

def lbtokg(lbs):
    return lbs * 0.45359237

def bmiCalc(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:
        return None
    return weight / height ** 2

def runBMIProgram():
    print('''Welcome to the BMI Calculator.
    \nChoose a number based on the Measurement units you will use    
    ''')
    valid=False
    while valid==False:
        print("Press 1 for Ft/In or 2 for Cm")
        heightChoice=input()
        if heightChoice=="1":
            #work out ft to cm
            userFeetInput=float(input("enter your height in feet "))
            userInchInput=float(input("enter your height in inches "))
            height=ftintom(userFeetInput, userInchInput)
            valid=True
        elif heightChoice=="2":
            height=float(input("Enter your height in CM "))
            valid=True
        else:
            print("Choose again")

    valid=False
    while valid==False:
        print("Press 1 for lbs or 2 for kg")
        weightChoice=input()
        if weightChoice=="1":
            #lbs
            weight=float(input("Enter your weight in lbs "))
            weight=lbtokg(weight)
            valid=True
        if weightChoice=="2":
            weight=float(input("Enter your weight in kg "))
            valid=True
        else:
            print("Error: Choose again")

    return bmiCalc(weight,height)






def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def isItRightTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2





if __name__ == '__main__':
    #run the BMI Program
    print(isItRightTriangle(5, 3, 4))
    print(isItRightTriangle(1, 3, 4))
    print(runBMIProgram())



