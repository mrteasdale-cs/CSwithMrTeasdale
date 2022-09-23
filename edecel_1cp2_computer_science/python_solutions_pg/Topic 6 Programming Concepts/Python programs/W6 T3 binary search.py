itemFound = False
searchFailed = False
names = ["Anna", "Bill", "David", "Faisal", "Jasmine", "Jumal", "Ken",
"Michela", "Pavel", "Rosa", "Stepan", "Tom", "Zac"]
itemSought = input("Search term: ")
first = 0
last = len(names)-1
while not (itemFound or searchFailed):
    print(first,last)
    midpoint = int((first + last)/2)
    if names[midpoint] == itemSought:
        itemFound = True
    else:
        if first > last:
            searchFailed = True
        else:
            if names[midpoint] < itemSought:
                first = midpoint + 1
            else:
                last = midpoint - 1

if itemFound:
    print("Item is at position ", midpoint)
else:
    print("Item is not in the array")
