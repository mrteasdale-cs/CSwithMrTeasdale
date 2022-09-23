def max(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = input("Enter number: ")
num2 = input("Enter number: ")
num3 = input("Enter number: ")

maxNum = max(num1, num2, num3)
print("maximum number is: ")
print(maxNum)
