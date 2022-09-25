## Changing Sex
## Program 10
## with comments

## The user is asked to enter the male report.
maleReport = str(input("Please enter the male report."))

## The stored string is changed using the replace function.
## Note that the program should account for the posibility that
## one of the words has a capital letter.
femaleReport = maleReport.replace("His ","Her ")
femaleReport = femaleReport.replace("He ","She ")
femaleReport = femaleReport.replace(" his "," her ")
femaleReport = femaleReport.replace(" he "," she ")

## The output is displayed on two lines.
print ("The female comment is:")
print (femaleReport)

## NOTE: Replace will replace a string even when it is
## part of a larger word.  To avoid "history" being changed
## to "hertory" spaces are added before the strings being
## found and replaced.
## This is only partially sucessful as punctuation directly
## after "his" or "he" ("his,") would result in the string
## not matching and therefore not being replaced.
## If you would like another challenge adapt the program to
## cope with punctuation.
