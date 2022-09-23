x = [7, 9, 6, 2, 4]
t = x[0]
k = x[0]
j = x[0]
for n in range(1,5):
    print(t,k,j,n,x[n])
    t = t + x[n]
    if x[n] > k:
        k = x[n]
    if x[n] < j:
        j = x[n]
print("k = " + str(k) + " j = " + str(j))
