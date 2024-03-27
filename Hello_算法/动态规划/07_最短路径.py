"""
07_最短路径 - 

Author: hanayo
Date： 2024/3/27
"""


def min_path_sum_dp(grid: list[list[int]]) -> int:
    """最小路径和：动态规划"""
    n, m = len(grid), len(grid[0])
    # 初始化dp表
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    # 初始化首行
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    # 初始化首列
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # 循环遍历,填满dp表
    for i in range(2, n):
        for j in range(2, m):
            dp[i][j] = min(dp[i-1][j], dp[i-1][j]) + grid[i][j]
    return dp[n-1][m-1]


def min_path_sum_comp(grid: list[list[int]]) -> int:
    """最小路径和：动态规划空间优化"""
    n, m = len(grid), len(grid[0])
    # 初始化dp表
    dp = [0] * m
    dp[0] = grid[0][0]
    # 初始化首行
    for j in range(1, m):
        dp[j] = dp[j-1] + grid[0][j]
    # 首列在遍历每行时初始化

    # 循环遍历,填满dp表
    for i in range(1, n):
        dp[0] = dp[0] + grid[i][0]
        for j in range(1, m):
            dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
    return dp[m-1]
