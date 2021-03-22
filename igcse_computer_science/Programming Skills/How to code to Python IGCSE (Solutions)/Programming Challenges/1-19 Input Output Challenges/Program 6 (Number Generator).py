## Number Generator (2 digits)
## Program 6
## with comments

## The user is  asked to enter two integers.

num1 = int(input())
num2 = int(input())


## To convert the digits into 10s and units perform the following
## calculation and display the result.

print (num1*10+num2)


## NOTE
## If you solved this problem by inputing two strings and concatenating
## the result, you have not completed the challenge.  This is because
## you are told "the program should then perform a calculation".
## This would therefore be wrong:
##   num1 = input()
##   num2 = input()
##   print (num1+num2)