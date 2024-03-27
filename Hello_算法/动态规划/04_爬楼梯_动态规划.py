"""
04_爬楼梯_动态规划 - 

Author: hanayo
Date： 2024/3/27
"""


def climbing_stairs(n: int):
    """爬楼梯：动态规划"""
    if n == 1 or n == 2:
        return n
    # 初始化dp表，用来存储每一个子问题的结果
    dp = [0] * (n+1)
    # 最小子问题的解
    dp[1], dp[2] = 1, 2
    # 遍历，逐步求较大问题的解
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def climbing_stairs_comp(n: int) -> int:
    """爬楼梯，空间优化后的动态规划"""
    if n == 1 or n == 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a+b
    return b