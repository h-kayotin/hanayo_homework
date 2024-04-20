"""
40_编辑距离 - 

Author: hanayo
Date： 2024/4/8
"""


def transform_str(s: str, t: str):
    """编辑距离，动态规划"""
    # dp[i][j]表示把s的前i个字符串变为t的前i个字符串的最小操作
    # 3种情况
    # 1. 添加： dp[i][j] = dp[i]dp[j-1] +1
    # 2. 删除： dp[i][j] = dp[i-1][j] + 1
    # 3. 替换： dp[i][j] = dp[i-1][j-1] + 1
    # 如果字符串相同时 dp[i][j] = dp[i-1][j-1]
    n, m = len(s), len(t)
    dp = [[0] * (m+1) for _ in range(n+1)]

    # 首行 首列
    for j in range(1, m+1):
        dp[0][j] = j
    for i in range(1, n+1):
        dp[i][0] = i

    # 状态转移
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[n][m]


def transform_str2(s: str, t: str):
    """编辑距离，空间优化"""
    n, m = len(s), len(t)
    dp = [0] * (m+1)

    for j in range(1, m + 1):
        dp[j] = j

    # 状态转移
    for i in range(1, n+1):
        left_up = dp[0]
        dp[0] += 1
        for j in range(1, m+1):
            tmp = dp[j]
            if s[i-1] == t[j-1]:
                dp[j] = left_up
            else:
                dp[j] = min(left_up, dp[j], dp[j-1]) + 1
            left_up = tmp
    return dp[m]


s = str(input())
t = str(input())
print(transform_str2(s, t))


