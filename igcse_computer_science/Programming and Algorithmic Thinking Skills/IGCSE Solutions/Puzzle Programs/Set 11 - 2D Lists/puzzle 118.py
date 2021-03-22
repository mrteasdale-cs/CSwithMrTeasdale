# Puzzle Program 118
grid = [ [5,8,6], [3,4,5], [6,1,0] ]
total = 0
grid[2][2] = 2
grid[0][2] = 3
grid[0][1] = grid[1][2]
for first in range(3):
    for second in range(3):
        total = total + grid[first][second]
print(total)

