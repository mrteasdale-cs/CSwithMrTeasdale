# Section 4 – Storing Multiple Values using Lists
# Example 38 – Input into a list using fixed and conditional loops
# Fixed loop

names = [""]*5
ages = [0]*5
for counter in range(5):
    names[counter] = str(input("Please enter name " + str(counter+1)))
    ages[counter] = int(input("Please enter " + names[counter] + "’s age"))