# Set the parameters (which are the legal age limits in Australia)
drivingAge = 16
drinkingAge = 18

age = int(input("Enter your age: ")) # Ask the user how old they are

if age < drivingAge: # If they are younger than 16
    print("You cannot drink or drive.")
elif age >= drinkingAge: # If they are 18 or older
    print("Party time - you can drink and drive (but not at the same time.)")
else: # If they are 16 or 17 years old
    print("You can drive, but you cannot drink yet.")