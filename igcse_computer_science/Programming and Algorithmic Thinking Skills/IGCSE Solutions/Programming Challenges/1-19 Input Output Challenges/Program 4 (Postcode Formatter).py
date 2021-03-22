## Postcode Formatter
## Program 4
## with comments

## Four inputs on four lines.
## Watch that you are using the correct types of variable,
## string, integer, integer and then string.

letterFirst = str(input())
numberFirst = int(input())
numberSecond = int(input())
letterSecond = str(input())


## Only one print lines is required this time.
## The clever bit in this program is how you add or remove
## the spaces between the stored values when they are printed.
## Watch how the + and , symbols are used.

print (letterFirst + str(numberFirst) , str(numberSecond) + letterSecond)

## Note - Python does not allow you to concatenate (join) a
## string with an integer using +
## This problem is easily solved by converting the integers to strings
## using the str() command.