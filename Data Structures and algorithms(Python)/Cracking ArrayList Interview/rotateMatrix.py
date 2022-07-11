matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
        ]
def rotate(matrix):
    n = len(matrix)
    #Transpose the matrix
    for i in range(0, n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    #Flip the matrix horizontally
    for i in range(0, n):
        for j in range(0, n//2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

    return matrix

print(rotate(matrix))
