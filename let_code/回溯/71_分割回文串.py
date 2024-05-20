"""
71_分割回文串 - 
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是
回文串  回文 串是向前和向后读都相同的字符串
 。返回 s 所有可能的分割方案。


Author: hanayo
Date： 2024/5/20
"""
from typing import List


def partition(self, s: str) -> List[List[str]]:
    ans = []
    path = []
    n = len(s)

    # start表示这段回文字符串开始的位置
    def dfs(i: int, start: int) -> None:
        if i == n:
            ans.append(path.copy())
            return

        # 不选i和i+1之间的逗号
        if i < n-1:
            dfs(i+1, start)

        # 选i和i+1之间的逗号
        t = s[start: i+1]
        if t == t[::-1]:
            path.append(t)
            dfs(i+1, i+1)
            path.pop()

    dfs(0, 0)
    return ans
