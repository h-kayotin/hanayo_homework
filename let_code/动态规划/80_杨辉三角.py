"""
80_杨辉三角 - 

Author: hanayo
Date： 2024/6/4
"""
from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows == 1:
        return [[1]]
    dp = [[1]]
    for i in range(1, numRows):
        cur = [1]
        for j in range(1, i):
            val = dp[i-1][j-1] + dp[i-1][j]
            cur.append(val)
        cur.append(1)
        dp.append(cur)
    return dp


def generate2(numRows: int) -> List[List[int]]:
    """优化"""
    dp = [[1]*(i+1) for i in range(numRows)]
    for i in range(2, numRows):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp
