"""
61_烂橘子 - 

在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

Author: hanayo
Date： 2024/5/10
"""


def orange_rotting(grid: list[list[int]]):
    row, col = len(grid), len(grid[0])
    # 烂橘子
    rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
    # 新鲜橘子
    fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
    time = 0
    while fresh:
        if not rotten:
            return -1
        # 计算每轮新的烂橘子
        rotten = {(i+di, j+dj) for i, j in rotten
                  for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]
                  if (i+di, j+dj) in fresh}
        # 从新鲜橘子集合中减去
        fresh -= rotten
        time += 1
    return time


set_a = {1,2,3}
set_b = {2,5,6}
print(set_b - set_a)