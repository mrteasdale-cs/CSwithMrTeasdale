# Puzzle Program 139
days = [4,6,4,5,8,2,4]
nights = []
for loop in range(5,0,-1):
    temp = days.pop(loop)
    nights.append(temp + loop)
print(nights)