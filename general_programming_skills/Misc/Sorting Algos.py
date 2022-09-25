# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:43:55 2020
@author: myran

=======================
Bubble Sort Algorithm
=======================
"""
def bubbleSort():
    myList = [99,45,64,4,1,19,76,5,8,3,5,4,2,9,1,12,87,2]
    swapped = True
    print("Unsorted List: ",myList)
    
    while swapped:
        swapped = False #no swaps so far
        for i in range(0,len(myList)-1):
            if myList[i] > myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]
                swapped = True # set swapped to true so the loop continues
                         
    print("Sorted List: ",myList)
'''
=================
Insertion sort
=================
'''
def insertionSort():
    myList2 = [76,5,8,3,5,4,2,9,1,12,87,2]
    print("Unsorted List: ",myList2)

    for x in range(1,len(myList2)):
        key=myList2[x]
        j=x-1

        while j >= 0 and key < myList2[j]:
            myList2[j+1] = myList2[j]
            j=j-1
            
        myList2[j+1] = key
        
    result="Sorted List: "+str(myList2)
    return result
    
print(insertionSort())