"""
74_搜索二维矩阵 - 

Author: hanayo
Date： 2024/5/21
"""
from typing import List


def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
    """二分查找，当成一维数组计算"""
    n, m = len(matrix), len(matrix[0])
    i, j = 0, m * n - 1
    while i <= j:
        mid = (i + j) // 2
        val = matrix[mid // m][mid % m]
        if val == target:
            return True
        elif target < val:
            j = mid - 1
        else:
            i = mid + 1
    return False


def search_matrix2(self, matrix: List[List[int]], target: int) -> bool:
    """排除法，每次比较右上角"""
    n, m = len(matrix), len(matrix[0])
    i, j = 0, m-1
    while i < n and j >= 0:
        if matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target:
            j -= 1
        else:
            return True
    return False



