# Puzzle Program 117
grid = [ [5,8,6], [3,4,5], [6,1,0] ]
for first in range(len(grid)-1):
    for second in range(3):
        print(grid[first][second],end='')
    print()

