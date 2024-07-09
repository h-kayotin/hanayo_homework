"""
122_两个字符串的最小ASCII删除和 - 

Author: hanayo
Date： 2024/7/9


dp[i][j]表示s1的前i-1个字符和s2的前j-1个字符的最小删除和

如果字符相同，党羽dp[i-1][j-1]

否则取前一位的小



"""


def minimum_delete_sum(self, s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]

    # 初始化首行
    for j in range(1, m+1):
        dp[0][j] = dp[0][j-1] + ord(s2[j-1])
    # 初始化首列
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0] + ord(s1[i-1])

    # 状态转移
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
    return dp[-1][-1]
