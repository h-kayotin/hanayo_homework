"""
09_完全背包问题 - 

Author: hanayo
Date： 2024/3/28
"""


def unbounded_knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    """完全背包：动态规划"""
    n = len(wgt)
    # 初始化 dp 表
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    # 状态转移
    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] > c:
                # 若超过背包容量，则不选物品 i
                dp[i][c] = dp[i - 1][c]
            else:
                # 不选和选物品 i 这两种方案的较大值
                dp[i][c] = max(dp[i - 1][c], dp[i][c - wgt[i - 1]] + val[i - 1])
    return dp[n][cap]


def unbounded_knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
    """完全背包：空间优化后的动态规划"""
    n = len(wgt)
    # 初始化 dp 表
    dp = [0] * (cap + 1)
    # 状态转移
    for i in range(1, n+1):
        # 正序遍历
        for c in range(1, cap+1):
            # 若超过背包容量，不选当前物品
            if wgt[i-1] > c:
                dp[c] = dp[c]
            # 不选和选物品 i 这两种方案的较大值
            else:
                dp[c] = max(dp[c], val[i-1] + dp[c-wgt[i-1]])
    return dp[cap]
