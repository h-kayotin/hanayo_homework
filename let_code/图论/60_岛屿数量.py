"""
60_岛屿数量 - 


给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。
Author: hanayo
Date： 2024/5/10
"""


def num_islands(grid: list[list[str]]):
    def dfs(matrix, i, j):
        """把所有相连的岛屿置0"""
        if not 0 <= i < len(matrix) or not 0 <= j < len(grid[0]) or matrix[i][j] == '0':
            return
        matrix[i][j] = '0'
        # 下
        dfs(matrix, i+1, j)
        # 右
        dfs(matrix, i, j+1)
        # 上
        dfs(matrix, i-1, j)
        # 左
        dfs(matrix, i, j-1)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count

