# Standard Algorithm
# Binary Search
# (Complex example, reading from file into 2D list)
# (List searched by surname, forename)

# Note that this was not included in the book but has be retained
# as a complex exam for talented students to examine.

def binarysearch(forename,surname):
    dataset = []
    with open('estates.csv','r') as people:
        for each in people.readlines():
            each = each[0:-1]
            temp = each.split(",")
            dataset.append(temp)

    lower = 0
    upper = len(dataset)-1
    found = False
    while lower<=upper and found==False:
        mid = int((lower+upper)/2)
        if dataset[mid][0] == forename and dataset[mid][1] == surname:
            found = True
        elif dataset[mid][1] < surname:
            lower = mid + 1
        elif dataset[mid][1] > surname:
            upper = mid - 1
        elif dataset[mid][0] < forename and dataset[mid][1] == surname:
            lower = mid + 1
        elif dataset[mid][0] > forename and dataset[mid][1] == surname:
            upper = mid - 1
    if found==True:
        print("Worth = ",dataset[mid][3])
    else:
        print("Name not found")


forename = str(input("Enter first name/s"))
surname = str(input("Enter surname"))
binarysearch(forename,surname)
