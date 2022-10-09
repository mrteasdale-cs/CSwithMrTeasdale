# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
# ===> Choose one line
#import math
import time

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
IMAGE_HAND  = "Hand"            # Images to be displayed once available
IMAGE_WALK = "Walk"
IMAGE_COUNTDOWN = "Countdown"

TIME_WALK = 10                  # Default time for walking
TIME_COUNTDOWN = 20             # Additional default countdown time

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
seconds = 0                 # For counting down the seconds
timesToTest = 3             # Times to run the test for

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# ===> Choose one line
while (timesToTest != 0):
#while (timesToTest < 3):
    print ("Showing image ... " + IMAGE_HAND)
    # ===> Choose one line
    time.sleep (15)
    #time.sleep (45)
    print ("Showing image ... " + IMAGE_WALK)
    # ===> Choose one line
    time.sleep (TIME_WALK)
    #time.sleep (20)
    # ===> Choose one line
    for seconds in range (TIME_COUNTDOWN, 0, -1):
    #for seconds in range (0, TIME_COUNTDOWN):
        print ("Showing image ... " + IMAGE_COUNTDOWN + " " + str (seconds))
        # ===> Choose one line
        time.sleep (1)
        #time.sleep (seconds)
    # ===> Choose one line
    timesToTest = timesToTest - 1
    #timesToTest = timesToTest + 1
print ("Happy crossing")
