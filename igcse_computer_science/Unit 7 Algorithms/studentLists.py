students = ['myran',"charlotte","andy","faye"]
weight = [82, 67, 78, 63]

name = input("Enter student name:")

print(students)
print(weight)

for i in range(0,len(students)):
    if name == students[i]:
        print(name,"is",weight[i],"kgs")
