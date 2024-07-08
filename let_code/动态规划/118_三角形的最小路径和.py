"""
118_三角形的最小路径和 - 

给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

Author: hanayo
Date： 2024/7/8
"""
from typing import List


def minimum_total(self, triangle: List[List[int]]) -> int:
    n = len(triangle)
    dp = []
    for i in range(n):
        dp.append([0] * (i+1))
    # 初始化首列
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
    for i in range(1, n):
        for j in range(1, len(triangle[i])-1):
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        dp[i][len(triangle[i])-1] = dp[i-1][len(triangle[i])-2] + triangle[i][len(triangle[i])-1]
    return min(dp[-1])

minimum_total(1,[[2],[3,4],[6,5,7],[4,1,8,3]])