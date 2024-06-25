"""
98_最长回文子串 - 
给你一个字符串 s，找到 s 中最长的
回文子串
。
https://leetcode.cn/problems/longest-palindromic-substring/solutions/2746518/javapython3cdong-tai-gui-hua-zhong-xin-k-frpr/?envType=study-plan-v2&envId=top-100-liked
Author: hanayo
Date： 2024/6/25
"""


def longest_palindrome(s: str) -> str:
    n = len(s)
    len_pali = 1
    start = 0
    # dp[j][i]表示子串s[j:i]是否为回文串
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, -1, -1):
            if i == j:
                dp[j][i] = True
            elif i == j + 1:
                dp[j][i] = (s[i] == s[j])
            else:
                dp[j][i] = (s[i] == s[j]) and dp[j+1][i-1]
            if dp[j][i] and (i-j+1) > len_pali:
                len_pali = i -j + 1
                start = j
    return s[start: start + len_pali]