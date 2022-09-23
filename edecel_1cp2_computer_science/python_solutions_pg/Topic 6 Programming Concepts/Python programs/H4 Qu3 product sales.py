sales = [
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]
        ]
totalsales = [0,0,0,0,0]
 
for product in range(5):
    print("Sales for product", product + 1)
    for month in range(3):
       print("Enter quantity for month ", month + 1,":") 
       sales[month][product] = int(input())
       totalsales[product] = totalsales[product] + sales[month][product]
print()
for product in range(5): 
    print("Total sales for product",product + 1, ":",totalsales[product])
