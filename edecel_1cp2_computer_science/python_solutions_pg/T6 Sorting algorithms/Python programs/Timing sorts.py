#program to compare the time taken to sort n random numbers using a bubble sort
# an insertion sort and a merge sort

import random
import time

    
#insertion sort
def insertionSort(alist,n):
    
    for j in range(1,n):
        nextnum = alist[j]
    
#insert nextnum into the sorted sequence numbers1[1..j-1]

        i = j - 1
        while i>=0 and alist[i]>nextnum:
           alist[i + 1] = alist[i]
           i = i - 1       
        alist[i + 1] = nextnum
    

#bubble sort

def bubbleSort(alist,n):
    m = n
    while m>1:
        for count in range (0, m - 1):
            if alist[count] > alist[count + 1]:
                temp = alist[count]
                alist[count] = alist[count+1]
                alist[count+1] = temp
        m = m - 1
             

def mergeSort(alist):
#    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
#    print("Merging ",alist)

#main program starts here
numbers1 = []
numbers2 = []
numbers3 = []
print("How many numbers do you want to sort? ")
n = int(input())
for count in range(0,n):
    numRange = n*10
    num  = int(random.randint(1,numRange))
    numbers1.append(num)
    numbers2.append(num)
    numbers3.append(num)
#print(numbers1)
#print(numbers2)
#print (numbers3)

#We now have three identical arrays of numbers to sort


clocktime1 = time.clock()
bubbleSort(numbers1,n)
clocktime2 = time.clock()
elapsedtime = (clocktime2 - clocktime1)* 1000
print ("The bubble sort took ", elapsedtime," thousandths of a second")

clocktime1 = time.clock()
insertionSort(numbers2,n)
clocktime2 = time.clock()
elapsedtime = (clocktime2 - clocktime1)* 1000
print ("The insertion sort took ", elapsedtime," thousandths of a second")

clocktime1 = time.clock()
mergeSort(numbers3)
clocktime2 = time.clock()
elapsedtime = (clocktime2 - clocktime1)* 1000
print ("The merge sort took ", elapsedtime," thousandths of a second")
#print(numbers3)

