# Puzzle Program 123
numList = [3,8,30,72,3,7,7,23,41,99,2,1,8,92]
limits = [ ]
limits.append(min(numList))
limits.append(max(numList))
manPlusMax = sum(limits)
print ("Minimum",limits[0],"+ Maximum",limits[1],"=",manPlusMax)