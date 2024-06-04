"""
79_爬楼梯 - 

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

Author: hanayo
Date： 2024/6/4
"""


def climb_stairs(self, n: int) -> int:
    """递归"""
    def dfs(i: int):
        if i == 1 or i == 2:
            return i
        count = dfs(i-1) + dfs(i-2)
        return count

    return dfs(n)


def climb_stairs_dp(self, n: int) -> int:
    """动态规划"""
    if n == 1 or n == 2:
        return n
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

