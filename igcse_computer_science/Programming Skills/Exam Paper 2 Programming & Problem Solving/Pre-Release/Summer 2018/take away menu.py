import random
menuitem = []
prices = []
itemcodes = []
total_cost = 0

def create_menu():
    file = open("menu.txt",'r').read().splitlines()
    for items in file:
        menuitem.append(items)
    file = open("prices.txt",'r').read().splitlines()
    for items in file:
        prices.append(items)
    for n in range(1,len(menuitem)+1):
        itemcodes.append("a"+str(n))

    print(itemcodes)
    print(menuitem)
    print(prices)

    for j in range(1, len(menuitem)):
        print("Code:", itemcodes[j], "\tMenu item:", menuitem[j], "\t\t\tPrice:", prices[j])


def order():
    stop = False
    order = []
    quantity = []
    daily_orders = [[], []]

    while stop == False:
        new_order = str(input("Enter the item code you want to order: "))
        qty = int(input("How many would you like? "))
        order.append(new_order)
        quantity.append(qty)
        end = input("Order more? (y or n)")
        if end == "n":
            stop = True
    uniquecode = random.randint(10000,99999)
    #daily_orders.append(uniquecode)
    return uniquecode, order, quantity

create_menu()
new_order = order()

print(new_order)
print(new_order[2][0])
print(len(new_order))

print("Unique Order No. ", new_order[0])
for i in range(len(new_order[1])):
    print("Menu item: ", new_order[1][i], "Quantity: ", new_order[2][i])
    total_cost = total_cost+(new_order[2][i])

#DOES NOT WORK YET
print("Total cost ", total_cost)

'''TASK 1 – Setting up the menu.
Set up a series of arrays to store the menu items and the prices, using the data supplied in the menu.
Devise an item code for each menu item and store these in another array. Output a new menu including
the item codes so that customers can place an order using the item codes.
TASK 2 – Placing an order.
Extend the program so that when a customer places their order from the menu you enter each item
code and the quantity. When the order is completely entered, a unique order code is generated. Display
the order ensuring that the unique order code, menu items and quantities are shown, along with the
item prices and the total cost of the order. Set up arrays for the day to store the unique order code and
the total cost of each order.
TASK 3 – Calculating daily takings and profit.
10% of the takings are profit. Extend the program to display the total daily takings and profit.
Modify your program to allow you to enter the percentage of the takings'''