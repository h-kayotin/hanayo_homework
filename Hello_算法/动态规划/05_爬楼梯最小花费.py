"""
05_爬楼梯最小花费 - 

Author: hanayo
Date： 2024/3/27
"""


def min_cost_climbing_stairs_dp(cost: list[int]) -> int:
    """爬楼梯最小代价：动态规划"""
    n = len(cost) - 1
    if n == 1 or n == 2:
        return cost[n]
    # 初始化dp表，用户存储子问题的解
    dp = [0] * (n+1)
    # 最小子问题的解
    dp[1], dp[2] = cost[1], cost[2]
    # 状态转移：从小问题逐步求大问题的解
    for i in range(3, n+1):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    return dp[n]


def min_cost_climbing_stairs_dp_comp(cost: list[int]) -> int:
    """爬楼梯最小代价：动态规划"""
    n = len(cost) - 1
    if n == 1 or n == 2:
        return cost[n]
    # 最小子问题的解
    a, b = cost[1], cost[2]
    # 状态转移：从小问题逐步求大问题的解
    for i in range(3, n + 1):
        a, b = b, min(a, b) + cost[i]
    return b
