def rotate_90(matrix):
    n = len(matrix)
    new_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[j][n-1-i] = matrix[i][j]
    return new_matrix

def rotate_180(matrix):
    n = len(matrix)
    new_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[n-1-i][n-1-j] = matrix[i][j]
    return new_matrix

def rotate_270(matrix):
    n = len(matrix)
    new_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[n-1-j][i] = matrix[i][j]
    return new_matrix

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(*matrix, sep='\n')
print()
print(*rotate_90(matrix), sep='\n')
print()
print(*rotate_180(matrix), sep='\n')
print()
print(*rotate_270(matrix), sep='\n')