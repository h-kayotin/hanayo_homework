"""
120_最大正方形 - 

Author: hanayo
Date： 2024/7/8
"""
from typing import List


def maximal_square(self, matrix: List[List[str]]) -> int:
    n, m = len(matrix), len(matrix[0])
    # dp[i][j]表示在以ij为右下角，最大正方形边长
    dp = [[0] * m for _ in range(n)]
    max_side = 0
    # 初始化首行
    for j in range(m):
        dp[0][j] = int(matrix[0][j])
        max_side = max(max_side, dp[0][j])
    # 初始化首列
    for i in range(n):
        dp[i][0] = int(matrix[i][0])
        max_side = max(max_side, dp[i][0])
    # 状态转移
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == '0':
                continue
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            max_side = max(max_side, dp[i][j])
    return max_side*max_side

