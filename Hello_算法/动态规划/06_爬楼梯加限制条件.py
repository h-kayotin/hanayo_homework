"""
06_爬楼梯加限制条件 - 

Author: hanayo
Date： 2024/3/27
"""


def climbing_stairs_constraint_dp(n: int) -> int:
    """带约束爬楼梯：动态规划"""
    if n == 1 or n == 2:
        return 1
    # 初始化 dp 表，用于存储子问题的解
    dp = [[0] * 3 for _ in range(n + 1)]
    # 初始状态
    dp[1][1], dp[1][2] = 1, 0
    dp[2][1], dp[2][2] = 0, 1
    # 状态转移过程
    for i in range(3, n+1):
        dp[i][1] = dp[i-1][2]
        dp[i][2] = dp[i-2][1] + dp[i-2][2]
    return dp[n][1] + dp[n][2]