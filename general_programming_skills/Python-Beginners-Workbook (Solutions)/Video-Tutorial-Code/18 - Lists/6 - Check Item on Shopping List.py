shopping_list = ["apples", "bananas", "carrots", "potatoes"]

item = input("What item would you like to check on the shopping list: ")

if item in shopping_list:
  print("Yes, " + item + " is on the shopping list.")
else:
    print("No, " + item + " is not on the shopping list.")
