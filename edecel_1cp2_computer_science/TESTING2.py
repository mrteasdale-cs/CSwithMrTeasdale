time = input("Please enter current time (24 hour clock): ")
charge = "0.00"
if time < "0600" and time > "2200":
    charge = "£0.00"
else:
    print("Vehicle types:")
    print("Motorcycle = type 1")
    print("Car = type 2")
    print("Goods vehicle = type 3")
    print("HGV and coaches = type 4")
    vehicleType = input("Please enter vehicle type (1, 2, 3 or 4: ")
    if vehicleType == "1":
        charge = "£1.00"
    elif vehicleType == "2":
        charge = "£2.00"
    elif vehicleType == "3":
        charge = "£2.50"
    elif vehicleType == "4":
        charge = "£5.00"
    else:
        print("Invalid vehicle type")
print(charge)