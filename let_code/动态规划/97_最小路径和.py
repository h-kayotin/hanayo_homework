"""
97_最小路径和 - 

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

Author: hanayo
Date： 2024/6/25
"""
from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for j in range(1,m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]

    return dp[n-1][m-1]

