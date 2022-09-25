# Puzzle Program 76
start = 1
for loop in range(1,6):
    start = start * 10
    mid = start%loop
    end = mid + loop
    start = end
print(start, mid, end)