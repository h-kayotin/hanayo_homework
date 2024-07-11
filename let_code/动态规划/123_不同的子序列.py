"""
123_不同的子序列 - 
给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数，结果需要对 109 + 7 取模。
Author: hanayo
Date： 2024/7/11
"""


def num_distinct(self, s: str, t: str) -> int:
    """"
    dp[i][j]表示t的前i个字符，可以由s的前j个字符组成的个数
    00是空字符串
    状态转移，如果s[i] = s[j]
    那么dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    否则
    dp[i][j] = dp[i][j-1]
    """
    m, n = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # 初始化首行,对于空字符，s中组成的方式只有1种
    for j in range(m + 1):
        dp[0][j] = 1
    # 首列都是0，因为对于空字符s，有0种方式组成t
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if t[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[-1][-1]