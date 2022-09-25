# Randomly create year temperature data
count = 1
import random

with open('yearTemperatures.txt','w') as temps:
    for loop in range(1,26):          #loop variable used to ensure temperatures rise from winter to summer
        temps.write(str(count))
        seed = int(loop*1.1)     # used to slightly increase the range of the initial temperatures for a week
        variation = random.randint(-6,4)     #introduces a random factor to the starting temperature for each week
        for loop in range(7):
            temps.write(","+str(seed+variation))    #makes the temperature vary by -2 to 2 from one day to the next
            variation = random.randint(-2,2)
        temps.write("\n")                          #ensures each week is written to a new line in the file
        count += 1
    for loop in range(27,0,-1):                #reverses above so that temperatures go back down from summer to winter
        temps.write(str(count))
        seed = int(loop*0.6)
        variation = random.randint(-5,5)
        for loop in range(7):
            temps.write(","+str(seed+variation))
            variation = random.randint(-2,2)
        temps.write("\n")
        count += 1