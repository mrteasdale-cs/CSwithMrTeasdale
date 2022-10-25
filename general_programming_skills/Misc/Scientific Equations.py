import cmath

def main():
    print('''Welcome to the Scientific Equation Calculator
    What would you like to begin with?
    
    1. Energy-Mass equation E=mc2
    2. Pythagoras Theorem
    3. Second Law of Thermodynamics
    4. Universal Law of Gravitation
    5. Quadratic Equations
    ''')
    choice = int(input("Enter a number"))

    if choice == 1:
        mass = int(input("Enter the mass of the object"))
        total_Energy = energy(mass)
        print("{:.2f}".format(float(total_Energy)), "MJ")
    elif choice == 2:
        a = int(input("Enter the value of side A"))
        b = int(input("Enter the value of side B"))
        print("C =", "{:.5f}".format(float(pythagoras(a, b))))
    elif choice == 3:
        thermodynamics()
    elif choice == 4:
        gravitation()
    elif choice == 5:
        # ax^2+bx+c=0
        print("Quadratic Eq Solver")
        a = int(input("Enter the value of A"))
        b = int(input("Enter the value of B"))
        c = int(input("Enter the value of C"))
        x = quadratic(a, b, c)
        print("X is ", x)
    else:
        print("invalid")


def energy(mass):
    c = 299792458
    e = float(mass*(c**2))
    return e

def pythagoras(a,b):
    c = cmath.sqrt(a**2 + b**2)
    return c

def thermodynamics():
    pass

def gravitation():
    pass

def quadratic(a,b,c):
    x = (-b + cmath.sqrt((b**2 - 4*a*c)))/2
    return x


main()

