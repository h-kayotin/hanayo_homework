"""
66_电话号码的字母组合 - 

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

Author: hanayo
Date： 2024/5/13
"""

mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n

        def dfs(i: int):
            if i == n:
                ans.append(''.join(path))
                return
            for c in mapping[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        dfs(0)
        return ans
