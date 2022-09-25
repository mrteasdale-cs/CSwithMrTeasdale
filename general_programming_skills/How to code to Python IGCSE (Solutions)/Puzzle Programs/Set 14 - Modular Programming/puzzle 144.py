# Puzzle Program 144
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

num1 = 8
num2 = 3
value = module4(num1,num2)
print(value)