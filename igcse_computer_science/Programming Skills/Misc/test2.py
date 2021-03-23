# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 22:02:48 2020

@author: myran
"""

myList = [1, 2, 4, 4, 1, 4, 2, 8, 2, 9, 9, 6, 6, 3, 12]
result=[]

for i in myList:
    if myList[i] not in result:
        print(myList[i])
        result.append(myList[i])
        

print("The list with unique elements only:", result)
print("\nOriginal list: ",myList)

myList = [1, 2, "in", True, "ABC"]

print(1 in myList) # outputs True
print("A" not in myList) # outputs True
print(3 not in myList) # outputs True
print(False in myList) # outputs False

beatles=[]
# step 1
beatles.append("John Lennon")
print("Step 1:", beatles)
# step 2
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)
# step 3
members=2
for i in range(members):
    name=input("Enter the name: ")
    beatles.append(name)
print("Step 3:", beatles)
# step 4
del beatles[3]
del beatles[4]
print("Step 4:", beatles)
# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))