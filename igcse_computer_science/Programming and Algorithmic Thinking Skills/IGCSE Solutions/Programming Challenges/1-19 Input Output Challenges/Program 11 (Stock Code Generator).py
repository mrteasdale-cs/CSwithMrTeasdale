## Stock Code Generator
## Program 11
## with comments

## The user is asked to enter a product name and year as strings.
productName = str(input("Please enter the product name."))
productYear = str(input("Please enter the year."))

## The stock code is calculated by concatenating sub-strings.
stockCode = productName[0:2] + productName[-2:] + productYear[0:1] + productYear[-1:]

## The output is displayed.
print ("The stock code for",productName,"is:")
print (stockCode)
