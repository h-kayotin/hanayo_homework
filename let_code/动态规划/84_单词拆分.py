"""
84_单词拆分 -

给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

Author: hanayo
Date： 2024/6/11
"""
from typing import List


def word_break(self, s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    for i in range(n):
        for j in range(i+1, n+1):
            if dp[i] and (s[i:j] in wordDict):
                dp[j] = True
    return dp[-1]
