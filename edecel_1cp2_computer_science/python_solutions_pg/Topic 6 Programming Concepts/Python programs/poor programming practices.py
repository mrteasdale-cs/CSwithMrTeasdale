x=True
while x:
    a=float(input("Enter temp in centigrade"))
    b=a*(9/5)+32
    print(b)
    c=input("Enter more temps? ")
    if c=='n':
        x=False
        
