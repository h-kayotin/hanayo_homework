"""
83_零钱兑换 - 

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

Author: hanayo
Date： 2024/6/7
"""
from math import inf
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    dp[i] 表示组成i金额，最少需要的硬币数量
    dp[i+1]的转移有以下情况：

    :param coins:
    :param amount:
    :return:
    """
    n = len(coins)
    dp = [[inf] * (amount+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i, val in enumerate(coins):
        for j in range(amount+1):
            # 硬币面值比当前数额大，不选
            if j < val:
                dp[i+1][j] = dp[i][j]
            # 选当前硬币
            else:
                dp[i+1][j] = min(dp[i][j], dp[i+1][j-val] + 1)
    res = dp[n][amount]
    return res if res < inf else -1


if __name__ == '__main__':
    print(coin_change([1,2,5], 11))
