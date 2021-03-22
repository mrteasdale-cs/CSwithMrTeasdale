# Section 4 – Storing Multiple Values using Lists
# Example 47 – Combining predefined functions and sum( )

milesCycled = [5,8,9,2,4,3,7,4,7,5,9,0]
bestDay = 0
average = 0

bestDay = milesCycled.index(max(milesCycled))
average = sum(milesCycled)/len(milesCycled)

print (max(milesCycled),"miles")
print ("were first cycled on day",bestDay+1)
print ("This was",max(milesCycled)-average)
print ("better than the average of",average)



