## Number Patterns - Part 2
## Program 37
## With Comments

## The program displays an initial message and asks for the start and
## end point for the list of numbers.

print("The following program will display odd numbers.")
start = int(input("Enter the first number in the list"))
end = int(input("Enter the last number in the list"))

## The program then uses the inputs in the range.
## Note that to display the last number one must be added on to the end variable.

print("Odd Numbers List")
for number in range(start,end+1,2):
    print(number)
