"""
02_爬楼梯_暴力搜索 - 

Author: hanayo
Date： 2024/3/27
"""


def dfs(i: int) -> int:
    """搜索"""
    # 显然dp[1] = 1 dp[2] = 2
    if i == 1 or i == 2:
        return i
    # dp[i] = dp[i-1] + dp[i-2]
    count = dfs(i-1) + dfs(i-2)
    return count


def climbing_stairs_dfs(n: int) -> int:
    """爬楼梯，搜索"""
    return dfs(n)
