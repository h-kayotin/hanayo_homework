"""
53_矩阵乘法 - 
如果A是个x行y列的矩阵，B是个y行z列的矩阵，把A和B相乘，其结果将是另一个x行z列的矩阵C。
简单来说就是cij = a的i行 * b的j列
Author: hanayo
Date： 2024/4/19
"""


def matrix_multiply(x, y, z, matrix1, matrix2):
    res_matrix = [[0]*z for _ in range(x)]

    for i in range(x):
        for j in range(z):
            row = matrix1[i]
            res = 0
            for idx in range(y):
                res += row[idx] * matrix2[idx][j]
            res_matrix[i][j] = res
    for row in res_matrix:
        for val in row:
            print(val, end=" ")
        print()


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    matrix1, matrix2 = [], []
    for _ in range(x):
        row = [int(x) for x in str(input()).split(" ")]
        matrix1.append(row)
    for _ in range(y):
        row = [int(x) for x in str(input()).split(" ")]
        matrix2.append(row)
    matrix_multiply(x, y, z, matrix1, matrix2)


main()