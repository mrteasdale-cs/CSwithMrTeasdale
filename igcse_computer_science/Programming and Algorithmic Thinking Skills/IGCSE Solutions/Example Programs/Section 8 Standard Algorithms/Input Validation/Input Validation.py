# Standard Algorithm
# Input Validation

number = int(input("Enter a value between 0 and 10"))
while number < 0 or number > 10:
    print("Your value was not between 0 and 10")
    number = int(input("Enter value again"))

print("Number =",number)