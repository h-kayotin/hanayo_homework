"""
27_旋转图像 - 

给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
Author: kayotin
Date 2024/4/5
"""


def rotate_matrix(matrix: list[list[int]]):
    """切片法"""
    my_ma = list(zip(*matrix))[::-1]
    res = []
    for i in range(-1, -len(my_ma)-1, -1):
        res.append(list(my_ma[i]))
    for i in range(len(matrix)):
        matrix[i] = res[i][::-1]
    print(matrix)



my_ma = [[1,2,3],[4,5,6],[7,8,9]]
rotate_matrix(my_ma)

