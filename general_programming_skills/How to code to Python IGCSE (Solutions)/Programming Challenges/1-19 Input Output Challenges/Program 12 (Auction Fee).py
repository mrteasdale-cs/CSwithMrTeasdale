## Auction Fee
## Program 12
## with commments

## The user is asked to input three costs:

## NOTE - Float variables should be used as we will expect the
## user to input values with decimal places.

print ("Please enter your three costs.")
cost1 = float(input())
cost2 = float(input())
cost3 = float(input())

## The costs must be totaled.
total = cost1 + cost2 + cost3

## The fee is 10% of the total rounded to zero decimal places.
fee = round(total/10,0)

## Display the results.
print ("The total cost is £"+str(total))
print ("The auction companies fee is £",str(fee))

## NOTE 2 - To display a £ sign next to the total and fee
## string concatenation is used as
##     print ("The total cost is £",total)
## would produce the output
##     "The total cost is £ 54.09"
## with an unwanted space after the £ sign.