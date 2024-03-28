"""
编辑距离问题 - 

Author: hanayo
Date： 2024/3/28
"""


def edit_distance_dp(s: str, t: str) -> int:
    """编辑距离：动态规划"""
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # 状态转移：首行首列
    for j in range(1, m+1):
        dp[0][j] = j
    for i in range(1, n+1):
        dp[i][0] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
    return dp[n][m]


print(edit_distance_dp("hello", "algo"))


def edit_distance_dp_comp(s: str, t: str) -> int:
    """编辑距离：空间优化后的动态规划"""
    n, m = len(s), len(t)
    dp = [0] * (m + 1)
    # 状态转移：首行
    for j in range(1, m + 1):
        dp[j] = j
    # 状态转移：其余行
    for i in range(1, n+1):
        leftup = dp[0]
        dp[0] += 1
        for j in range(1, m+1):
            temp = dp[j]
            if s[i-1] == s[j-1]:
                dp[j] = leftup
            else:
                dp[j] = min(dp[j-1], dp[j], leftup) + 1
            leftup = temp
    return dp[m]
