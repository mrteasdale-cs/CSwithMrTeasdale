# Section 7 – File Handling
# Example 62 – Reading from a Text File into a 2D List

names = []

with open('Friends.txt','r') as pals:

    for each in pals.readlines():

        each = each[0:-1]
        temp = each.split(" ")
        names.append(temp)

print(names)
