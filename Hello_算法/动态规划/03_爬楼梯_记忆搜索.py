"""
03_爬楼梯_记忆搜索 - 

Author: hanayo
Date： 2024/3/27
"""


def dfs(i: int, mem: list[int]) -> int:
    """记忆化搜索"""
    # 已知dp[1] 和 dp[2]，
    if i == 1 or i == 2:
        return i
    # 如果dp[i]存在，就直接返回
    if mem[i] != -1:
        return mem[i]
    # dp[i] = dp[i-1] + dp[i-2]
    count = dfs(i-1, mem) + dfs(i-2, mem)
    # 记录 dp[i]
    mem[i] = count
    return count


def climbing_stairs_dfs_mem(n: int) -> int:
    """爬楼梯：记忆化搜索"""
    mem = [-1] * (n+1)
    return dfs(n, mem)