"""
99_最长公共子序列 - 

Author: hanayo
Date： 2024/6/27
"""


def longest_common_subsequence(self, text1: str, text2: str) -> int:
    n, m = len(text1), len(text2)
    dp = [[0] * m for _ in range(n)]
    if text1[0] == text2[0]:
        dp[0][0] = 1
    # 初始化首列
    for i in range(1, n):
        if text1[i] == text2[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i-1][0]
    # 初始化首行
    for j in range(1, m):
        if text1[0] == text2[j]:
            dp[0][j] = 1
        else:
            dp[0][j] = dp[0][j-1]
    # 状态转移
    for i in range(1, n):
        for j in range(1, m):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n-1][m-1]

