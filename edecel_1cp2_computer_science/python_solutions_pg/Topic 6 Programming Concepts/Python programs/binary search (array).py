#binary search of an array

#remember that the first element of the array is A[0], not A[1]
A = ["Anna","Bill","David","Faisal","Jasmine","Jumal",
     "Ken","Michela","Pavel","Rosa","Stepan","Tom","Zac"]
itemSought=input("Please enter name to search for: ")
itemFound = 0
searchFailed = False
lastIndex = len(A)-1
firstIndex = 0

while (not itemFound) and (not searchFailed):
    midpoint = int((firstIndex + lastIndex)/2)
    print("firstIndex, lastIndex, midpoint, name", firstIndex, lastIndex, midpoint, A[midpoint])
    if A[midpoint] == itemSought:
        itemFound = 1
    else:
        if firstIndex > lastIndex:
            searchFailed = True
        else:
            if A[midpoint] < itemSought:
                firstIndex = midpoint + 1      
            else:
                lastIndex = midpoint - 1

#endwhile
if itemFound:
    print("item is at position ", midpoint)
else:
    print("item is not in the array")
    
input("\nPress ENTER to exit program ")
    
