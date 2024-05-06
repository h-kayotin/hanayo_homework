"""
55_摘樱桃 -

给你一个 n x n 的网格 grid ，代表一块樱桃地，每个格子由以下三种数字的一种来表示：

0 表示这个格子是空的，所以你可以穿过它。
1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
-1 表示这个格子里有荆棘，挡着你的路。
请你统计并返回：在遵守下列规则的情况下，能摘到的最多樱桃数：

从位置 (0, 0) 出发，最后到达 (n - 1, n - 1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为 0 或者 1 的格子）；
当到达 (n - 1, n - 1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为 0 ）；
如果在 (0, 0) 和 (n - 1, n - 1) 之间不存在一条可经过的路径，则无法摘到任何一个樱桃。

Author: hanayo
Date： 2024/5/6
"""
from functools import cache
from math import inf


def cherry_pick(grid: list[list[int]]):
    """
    dp[i][j]取决于左和上，也就是dp[i][j-1]或者dp[i-1[j]
    """
    @cache
    def dfs(t, j, k):
        if j < 0 or k < 0 or t < j or t < k or grid[t - j][j] < 0 or grid[t - k][k] < 0:
            return -inf
        if t == 0:
            return grid[0][0]
        return max(dfs(t - 1, j, k), dfs(t - 1, j, k - 1), dfs(t - 1, j - 1, k), dfs(t - 1, j - 1, k - 1)) + \
            grid[t - j][j] + \
            (grid[t - k][k] if k != j else 0)
    n = len(grid)
    return max(dfs(n*2 - 2, n-1, n-1), 0)


if __name__ == '__main__':
    cherry_pick([[0, 1, -1], [1, 0, -1], [1, 1, 1]])
