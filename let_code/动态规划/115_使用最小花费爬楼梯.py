"""
115_使用最小花费爬楼梯 - 
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。
Author: hanayo
Date： 2024/7/4
"""
from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    n = len(cost)
    # dp[i]表示爬n个台阶的最小花费
    dp = [0] * (n+1)
    dp[2] = min(cost[0], cost[1])
    # 状态转移
    # dp[i] = min(dp[i-1], dp[i-2])
    for i in range(3, n+1):
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    return dp[n]


if __name__ == '__main__':
    print(min_cost_climbing_stairs([10,15,20]))