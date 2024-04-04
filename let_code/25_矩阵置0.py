"""
25_矩阵置0 -

给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

Author: hanayo
Date： 2024/4/4
"""


def set_zeros(matrix: list[list[int]]):
    """模拟"""
    n, m = len(matrix), len(matrix[0])
    zero_row, zero_col = set(), set()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)

    for i in range(n):
        for j in range(m):
            if i in zero_row or j in zero_col:
                matrix[i][j] = 0


def set_zeros2(matrix: list[list[int]]):
    """原地，用第一行和第一列来记录是否有0"""
    flag_col = False
    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        if matrix[i][0] == 0:
            flag_col = True
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0], matrix[0][j] = 0, 0

    for i in range(n-1, -1, -1):
        for j in range(m-1, 0, -1):
            if matrix[i][0] ==0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if flag_col:
            matrix[i][0] = 0


