def isToeplitz():
    matrix = [[1,2,3,4],[5,2,2,3],[9,5,1,2]]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row > 0 and col > 0 and matrix[row][col] != matrix[row-1][col-1]:
                return False
    return True            
                

print(isToeplitz())