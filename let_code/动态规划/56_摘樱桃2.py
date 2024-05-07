"""
56_摘樱桃2 - 
给你一个 rows x cols 的矩阵 grid 来表示一块樱桃地。 grid 中每个格子的数字表示你能获得的樱桃数目。

你有两个机器人帮你收集樱桃，机器人 1 从左上角格子 (0,0) 出发，机器人 2 从右上角格子 (0, cols-1) 出发。

请你按照如下规则，返回两个机器人能收集的最多樱桃数目：

从格子 (i,j) 出发，机器人可以移动到格子 (i+1, j-1)，(i+1, j) 或者 (i+1, j+1) 。
当一个机器人经过某个格子时，它会把该格子内所有的樱桃都摘走，然后这个位置会变成空格子，即没有樱桃的格子。
当两个机器人同时到达同一个格子时，它们中只有一个可以摘到樱桃。
两个机器人在任意时刻都不能移动到 grid 外面。
两个机器人最后都要到达 grid 最底下一行。


Author: hanayo
Date： 2024/5/7
"""
from functools import cache

"""问题分析
机器人只能往下走，每次有3个选择，左下、下、右下
2个机器人，分别从左上和右上出发。
每走一步都是上一步的子问题，所以使用递归

状态定义
dfs(i,j,k)表示A从(i,j)出发，B从(i,k)出发所获取的樱桃最大值

第一步一共有9种情况，其中一种是
A往下，B往做下，子问题是A从(i+1,j)出发，B从(i+1,k-1)出发，也就是dfs(i+1,j,k-1)
9种情况取最大值，加上grid[i][j] grid[i][k]，就得到了dfs(i,j,k)

dfs(i,j,k) = val + max(9种情况）
val = grid[i][j] + grid[i][k] if j != k else grid[i][j]

递归边界：也就是出界的情况
入口：dfs(0,0,n-1)
"""


def cherry_pick(grid: list[list[int]]):
    n, m = len(grid), len(grid[0])

    @cache
    def dfs(i, j, k):
        if i == n or j < 0 or j >= m or k < 0 or k >= m:
            return 0
        return max(dfs(i + 1, j2, k2) for j2 in (j - 1, j, j + 1) for k2 in (k - 1, k, k + 1)) \
            + grid[i][j] + (grid[i][k] if k != j else 0)
    return dfs(0, 0, m-1)