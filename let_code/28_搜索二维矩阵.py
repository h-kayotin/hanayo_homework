"""
28_搜索二维矩阵 - 
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列
Author: hanayo
Date： 2024/4/8
"""


def search_matrix(matrix: list[list[int]], target: int):
    """穷举"""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
    return False


def search_matrix2(matrix: list[list[int]], target: int):
    """二叉搜索树"""
    i, j = len(matrix) - 1, 0
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] > target:
            i -= 1
        elif matrix[i][j] < target:
            j += 1
        else:
            return True
    return False
