"""
113_斐波那契数 - 
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。
Author: hanayo
Date： 2024/7/4
"""


def fib(self, n: int) -> int:
    dp = [0] * (n+2)
    dp[0], dp[1] = 0, 1
    if n <= 2:
        return dp[n]
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
