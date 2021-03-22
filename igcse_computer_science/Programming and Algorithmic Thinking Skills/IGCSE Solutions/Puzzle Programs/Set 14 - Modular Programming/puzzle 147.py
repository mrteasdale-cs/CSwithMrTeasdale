# Puzzle Program 147
def module1(first,second,third):
    volume = first * second * third
    print("Volume =",volume)

def module2(monday):
    monday = monday/10
    return monday

def module3(blue,red):
    total = 0
    for counter in range(blue,red):
        total = total + 2
    print(total)
    return total

def module4(up,down):
    middle = up%down
    top = int(up/down)
    total = middle + top
    return total

num1 = 2
num2 = 5
num3 = 8
module1(num1,module3(num1,num2),module2(5*num3))