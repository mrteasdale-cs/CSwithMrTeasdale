count = 0
weight = 0
accept = 0
reject = 0

while (count <= 5):
    count += 1
    weight = int(input("Enter weight of parcel: "))

    if (weight < 100) or (weight > 515):
        reject += 1
    else:
        accept += 1

print("Number accepted: ", accept)
print("Number rejected: ", reject)

