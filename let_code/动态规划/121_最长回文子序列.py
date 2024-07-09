"""
121_最长回文子序列 - 
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。


Author: hanayo
Date： 2024/7/9
"""


def longest_palindrome_subseq(self, s: str) -> int:
    """回文子串指的是，正读反读都一样的字符串"""
    # dp[i][j]字符串在[i,j]范围内的最长回文子序列长度
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][-1]