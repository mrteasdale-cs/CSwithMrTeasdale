#____task 1 setup the lists
components = ['Processor', 'RAM','Storage','Screen Size','Tower Type','Number of Ports']
component_names = ['p3','p5','p7','16GB','32GB','1TB','2TB','19','23','Mini Tower', 'Midi Tower', '2', '4']
item_prices = [100, 120, 200, 75, 150, 50, 100, 65, 120, 40, 70, 10, 20]
#stock levels
orig_stock_level = [12, 23, 0, 12, 43, 21, 2, 1, 4, 7, 9, 3, 2]
stock_level = [12, 23, 0, 12, 43, 21, 2, 1, 4, 7, 9, 3, 2]

#Task3
num_orders = 0
todays_total = 0

#Todays Date
import datetime
now = datetime.datetime.now()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
print("Today is ", months[now.month -1], now.day)

print("Input customer name ")
name = input()
cust_orderNum = 1000
exit = False
while not exit:
    # New customer
    cust_total = 0
    cust_prices = []
    cust_choices = []
    #____Task 2_____________________
    print("Processor options: "+ str(component_names[0:3]))
    user_choice = input()

    # Validation
    while user_choice not in component_names[0:3] or stock_level[component_names.index(user_choice)] == 0:
        print("Choice out of stock or invalid option")
        user_choice = input()

    #find out index of choice
    choice_position = component_names.index(user_choice)
    #it is valid update stock number now
    stock_level[choice_position] = stock_level[choice_position] - 1
    #append item to list
    cust_choices.append(user_choice)
    cust_prices.append(item_prices[choice_position])
    cust_total = cust_total + item_prices[choice_position]
    #___________
    #loop through rest of components
    for pos in range(1, len(components)):
        this_comp = components[pos]
        #move through the list to get correct positions of items and options
        # e.g. RAM should be index 3 and 4 (stop at index 5)

        low_pos = pos*2+1
        high_pos = pos*2+3
        print(this_comp, "Options are: ", component_names[low_pos:high_pos])
        user_choice = input()
        #Validate
        choice_position = component_names.index(user_choice)
        while user_choice not in component_names[low_pos:high_pos] and stock_level[component_names] < 0:
            print("Choice out of stock or invalid option")
            user_choice = input()
        # find out index of choice
        choice_position = component_names.index(user_choice)
        # it is valid update stock number now
        stock_level[choice_position] = stock_level[choice_position] - 1
        # append item to list
        cust_choices.append(user_choice)
        cust_prices.append(item_prices[choice_position])
        cust_total = cust_total + item_prices[choice_position]

    print("==ORDER==")
    print("Customer name:", name)
    print(str(months[now.month]))
    print("\nTotal cost of PC: ", str(cust_total*1.2))
    print("Components chosen: ", cust_choices)
    print("Prices: ", cust_prices)

    #Task 3
    num_orders = num_orders + 1
    todays_total = todays_total+cust_total*1.2

    print("\nOrder again? y or n")
    ok =  input().lower()
    if ok in ['n','no']:
        exit = True

print("Number of orders today:", num_orders)
for i in range(1, len(orig_stock_level), 1):
    print(component_names[i], orig_stock_level[i] - stock_level[i], end=', ')
#value of all orders
print("\nToday's total value: " + str(todays_total))









