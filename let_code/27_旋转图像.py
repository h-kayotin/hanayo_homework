"""
27_旋转图像 - 

给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
Author: kayotin
Date 2024/4/5
"""
import copy


def rotate_matrix(matrix: list[list[int]]):
    """切片法"""
    my_ma = list(zip(*matrix))[::-1]
    res = []
    for i in range(-1, -len(my_ma)-1, -1):
        res.append(list(my_ma[i]))
    for i in range(len(matrix)):
        matrix[i] = res[i][::-1]
    print(matrix)


def rotate_matrix2(matrix: list[list[int]]):
    """辅助矩阵"""
    n = len(matrix)
    tmp = copy.deepcopy(matrix)

    for i in range(n):
        for j in range(n):
            matrix[j][n-1-i] = tmp[i][j]


def rotate_matrix3(matrix: list[list[int]]):
    """原地修改"""
    n = len(matrix)
    for i in range(n // 2):
        for j in range( (n+1) // 2):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = tmp


my_ma = [[1,2,3],[4,5,6],[7,8,9]]
rotate_matrix(my_ma)

