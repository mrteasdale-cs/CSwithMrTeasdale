## For Sale - Part 2
## Program 47
## With Comments

## In part 2, a set of prices are stored as integers.
items = ["Mountain Bike","Ski Jacket","Electric Guitar","PS3 - 500Gb","Badminton Racquet"]
prices = [200,67,330,120,15]

## A loop is used to display the values in both lists.
## A £ sign is concatenated onto the prices. Note that this requires the
## prices to be converted to strings as concatenation only works when both
## values are strings.
for index in range(5):
    print(items[index]," - £"+str(prices[index]))



## Additional Note
## It would be easier to simply store the prices as strings.
##   items = ["Mountain Bike","Ski Jacket","Electric Guitar","PS3 - 500Gb","Badminton Racquet"]
##   prices = ["£200","£67","£330","£120","£15"]
##   for index in range(5):
##       print(items[index]," -",prices[index])
##
## However, it is important that values are stored using an appropraite data type.
## It would a lot more harder to calculate the total price of the items, for
## example, if the prices were stored as text.