# Puzzle Program 105
nameList1 = ["Bob","Derek","Fred","Usman","Abubakar"]
nameList2 = ["Mary","Nida","Jill","Tracy","Helen"]
temporary = ""
for names in range(5):
	if nameList1[names][0:1] < nameList2[names][0:1]:
		temporary = nameList1[names ]
		nameList1[names] = nameList2[names]
		nameList2[names] = temporary
print(nameList1)
print(nameList2)