## Postcode Formatter (Part 2)
## Program 7
## with comments

letterFirst = str(input())
numberFirst = int(input())
numberSecond = int(input())
letterSecond = str(input())


## The upper() function is applied to both of the string
## variables 'letterFirst' and 'letterSecond'.
## This ensures the output is always in uppercase, even
## when the input is not.

print (letterFirst.upper() + str(numberFirst) , str(numberSecond) + letterSecond.upper())

