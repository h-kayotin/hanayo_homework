"""
08_经典背包问题 - 

Author: hanayo
Date： 2024/3/28
"""


def knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    """0-1 背包：动态规划"""
    n = len(wgt)
    # 初始化 dp 表
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    # 状态转移
    for i in range(1, n+1):
        for c in range(1, cap+1):
            # 第i个物品装不下，所以还是上一行的值
            if wgt[i-1] > c:
                dp[i][c] = dp[i-1][c]
            # 装得下的情况，首先背包容量要减去wgt[i-]
            # 此时的最优解 + 该商品价值就是 dp[i-1][c-wgt[i-1]] + val[i-1]
            else:
                dp[i][c] = max(dp[i-1][c], dp[i-1][c-wgt[i-1]] + val[i-1])
    return dp[n][cap]


def knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
    """0-1 背包：空间优化后的动态规划"""
    n = len(wgt)
    # 初始化 dp 表
    dp = [0] * (cap + 1)
    # 状态转移
    for i in range(1, n+1):
        # 倒序遍历
        for c in range(cap, 0, -1):
            if wgt[i-1] > c:
                dp[c] = dp[c]
            else:
                dp[c] = max(dp[c], val[i-1] + dp[c-wgt[i-1]])
    return dp[cap]


