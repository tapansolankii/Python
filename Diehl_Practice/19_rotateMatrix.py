def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_matrix(matrix)
print(matrix)


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\19_rotateMatrix.py
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 