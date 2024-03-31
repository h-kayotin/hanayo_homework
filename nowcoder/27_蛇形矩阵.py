"""
27_蛇形矩阵 - 

Author: kayotin
Date 2024/3/31
"""


def snake_matrix(n: int):
    col_max = n

    res = []
    # 首行
    row = [1] * n
    for i in range(1, n):
        num = row[i-1] + i + 1
        row[i] = num
    res.append(row)

    # 循环填每一行
    for i in range(1, n):
        col_max -= 1
        row = []
        for j in range(col_max):
            num = res[i-1][j] + j + i
            row.append(num)
        res.append(row)

    for row in res:
        for idx, val in enumerate(row):
            if idx == len(row)-1:
                print(val)
            else:
                print(val, end=" ")


snake_matrix(4)