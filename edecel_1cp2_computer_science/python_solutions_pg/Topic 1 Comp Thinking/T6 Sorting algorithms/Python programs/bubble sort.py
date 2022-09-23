# Program to perform a bubble sort
# Define the list of names
userName = ["Carl","Tamsin","Eric","Zoe","Alan","Mark"]
numItems = 6
while numItems>1:
    for count in range(5):
        if userName[count] > userName[count+1]:
            temp = userName[count] 
            userName[count] = userName[count+1] 
            userName[count+1] = temp
    numItems = numItems-1
#endwhile
print(userName)
