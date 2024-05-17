"""
69_括号生成 - 
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
Author: hanayo
Date： 2024/5/17
"""
from typing import List


def generate_parenthesis(self, n: int) -> List[str]:
    """从2n中选n个位置放左括号"""
    m = n * 2
    ans = []
    path = [''] * m

    def dfs(i: int, open: int) -> None:
        if i == m:
            ans.append(''.join(path))
            return
        # open表示左括号的个数，如果左小于n，表示可以选左括号
        if open < n:
            path[i] = '('
            dfs(i+1, open+1)
        # i - open 就是右括号个数，右小于左，表示可以选右括号
        if i - open < open:
            path[i] = ')'
            dfs(i+1, open)

    dfs(0, 0)
    return ans



