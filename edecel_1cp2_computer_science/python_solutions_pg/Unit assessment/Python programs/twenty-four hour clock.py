#Convert 24 hour clock format to 12 hour format

hour = int(input("Enter hour between 0 and 23: "))
if hour == 0:
    print("Midnight")
elif hour < 12:
    print(str(hour) + "am")
elif hour == 12:
    print ("Midday")
else:
    hour = hour - 12
    print(str(hour) + "pm")
