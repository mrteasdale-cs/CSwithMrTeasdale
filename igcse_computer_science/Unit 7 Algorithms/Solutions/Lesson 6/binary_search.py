#binary search of an array

#remember that the first element of the array is A[0], not A[1]
A = ["Anna","Bill","David","Faisal","Jasmine","Jumal","Ken","Michela","Pavel","Rosa","Stepan","Tom","Zac"]
itemSought=input("Please enter name to search for: ")
itemFound = 0
searchFailed = 0
top = len(A)-1
bottom = 0

while (not itemFound) and (not searchFailed):
    midpoint = int((top + bottom)/2)
    print("top, bottom, midpoint", top, bottom, midpoint)
    if A[midpoint]==itemSought:
        itemFound = 1
    else:
        if bottom > top:
            searchFailed = 1
        else:
            if A[midpoint]<itemSought:
                bottom = midpoint + 1      
            else:
                top = midpoint - 1

#endwhile
if itemFound:
    print("item is at position ",midpoint)
else:
    print ("item is not in the array")