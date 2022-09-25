# Puzzle Program 119
grid = [ [5,8,6], [3,4,5], [6,1,0] ]
for second in range(2,-1,-1):
    for first in range(2,-1,-1):
        print(grid[first][second],end='')
    print()

