"""
114_第 N 个泰波那契数 - 
泰波那契序列 Tn 定义如下：

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
Author: hanayo
Date： 2024/7/4
"""


def tribonacci(self, n: int) -> int:
    dp = [0, 1, 1]
    if n < 3:
        return dp[n]
    dp += [0] *(n-2)
    for i in range(3, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    return dp[n]


if __name__ == '__main__':
    print(tribonacci(1,25))