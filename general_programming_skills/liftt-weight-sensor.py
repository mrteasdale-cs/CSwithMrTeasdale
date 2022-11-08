def liftWeightSensor():
    print("Detecting when too many people in the lift")
    print("Enter current weight in KG: ")
    weight = float(input())

    if weight> 350:
        print("Lift to full, please exit.")
    else:
        print("Lift moving.")

