age = int(input("Enter your age: "))

if age >= 18:
    print("You can watch R-rated movies")
elif age <= 17 and age >= 15:
    print("You can watch MA-rated movies")
else:
    print("You can watch G-rated, PG-rated and M-rated movies")


