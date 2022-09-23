ID = [45, 33, 27, 88, 103, 66, 71]
numberSought = int(input ("Please enter ID number to find: "))
found = False
n = len(ID)
k = 0
while not found and k < n:
    print("number sought", numberSought, "k", k, "ID[k]", ID[k])
    if numberSought == ID[k]:
        found = True
    k = k + 1
if found:
    print("ID is in the list at index ", k - 1)
else:
    print("ID is not in the list")
