"""
117_不同路径2 - 

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

Author: hanayo
Date： 2024/7/8
"""
from typing import List


def unique_paths_with_obstacles(obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0]:
        return 0
    n, m = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * m for _ in range(n)]
    # 初始化首行
    dp[0][0] = 1
    for j in range(1, m):
        if obstacleGrid[0][j]:
            dp[0][j] = 0
            continue
        dp[0][j] = dp[0][j-1]
    # 初始化首列
    for i in range(1, n):
        if obstacleGrid[i][0]:
            dp[i][0] = 0
            continue
        dp[i][0] = dp[i-1][0]

    # 状态转移
    for i in range(1, n):
        for j in range(1, m):
            if obstacleGrid[i][j]:
                dp[i][j] = 0
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n-1][m-1]


if __name__ == '__main__':
    unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]])
