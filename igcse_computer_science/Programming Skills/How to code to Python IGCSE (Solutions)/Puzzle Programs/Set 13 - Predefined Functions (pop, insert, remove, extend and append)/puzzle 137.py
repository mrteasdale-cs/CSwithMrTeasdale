# Puzzle Program 137
days = [4,6,4,5,8,2,4]
nights = []
temp = days.pop(2)
nights.append(temp)
nights.append(temp+1)
nights.append(temp+2)
print(nights)