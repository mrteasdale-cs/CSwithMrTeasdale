## Number Patterns - Part 3
## Program 39
## With Comments

print("The following program will display odd numbers.")
start = int(input("Enter the first number in the list"))

## A while loop is used to ensure that the vakue entered for end is 20 more
## the value entered for start.

end = int(input("Enter the last number in the list"))
while end < start+20:
    print("Sorry, the number must be at least "+str(start)+"+20")
    end = int(input("Enter re-enter the number"))


## As before the numbers are displayed using the start and end variable in the range.

print("Odd Numbers List")
for number in range(start,end+1,2):
    print(number)
