fruit = ["apples", "bananas", "grapefruit", "kiwi", "melon"]
searchTerm = "grapefruit"

for item in fruit:
    if item == searchTerm:
        print("found")


i = 0
itemFound = False
while i < len(fruit) and not itemFound:
    if fruit[i] == searchTerm:
        print("found")
        itemFound = True
    i = i + 1
    
    
