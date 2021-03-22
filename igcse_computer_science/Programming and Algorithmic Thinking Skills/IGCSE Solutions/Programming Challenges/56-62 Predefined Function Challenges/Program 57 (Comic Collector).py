## Comic Collector
## Program 57
## With Comments

## The program starts by storing Anita's original list of comics.
comics = [1,2,3,7,8,9,10,16]

## The user is asked to enter the new comics in a suitable format.
print("Please enter the new comics separated by a space")
print("For example: 4 5 8 12 17")
new = str(input())

## Now split (using the space character) the inputed string into
## a new list.
newComicsList = new.split(" ")

## Next combine the two lists by extending the original list.
comics.extend(newComicsList)

## Display the full comic collection
print("The issues of Super Rat now owned are:")
print(comics)

## Note: The above solution is not perfect as the final list contains
## a mixture of integers and strings.
## To perfect the program each item of the new list should be converted
## to an integer before the original list is extended.
## This can be done with a simple loop and the int() function.

## for comic in range(len(newComicsList)):
##     newComicsList[comic] = int(newComicsList[comic])
