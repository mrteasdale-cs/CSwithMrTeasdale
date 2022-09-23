validAge = False
age = 0
while not validAge:
    age = int(input("Enter your age: "))
    if age >= 0 and age <= 120:
        validAge = True
