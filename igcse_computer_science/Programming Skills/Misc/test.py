#haribo = []
name = []
exit = "n"
while exit != "y":
  name = str(input("enter names for list"))
  exit = input("do you want to exit? type y")
  name.append(name)

print(name)
