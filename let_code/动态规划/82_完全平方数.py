"""
82_完全平方数 - 
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
Author: hanayo
Date： 2024/6/7
"""
import math


def num_squares(n: int) -> int:
    dp = [i for i in range(n+1)]
    for i in range(2, n+1):
        for j in range(1, int(math.sqrt(i))+1):
            dp[i] = min(dp[i], dp[i-j*j] + 1)
    return dp[n]
