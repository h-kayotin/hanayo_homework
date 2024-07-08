"""
119_下降路径最小和 - 

Author: hanayo
Date： 2024/7/8
"""
from typing import List


def min_falling_path_sum(self, matrix: List[List[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    dp = [[0] * m for _ in range(n)]
    # 初始化首行
    for j in range(m):
        dp[0][j] = matrix[0][j]

    for i in range(1, n):
        for j in range(m):
            if j == 0:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j+1])
            elif j == m-1:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])
            dp[i][j] += matrix[i][j]
    return min(dp[-1])
