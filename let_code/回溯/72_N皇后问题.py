"""
72_N皇后问题 - 

Author: hanayo
Date： 2024/5/20
"""
from typing import List


def solve_queens(self, n: int) -> List[List[str]]:
    ans = []
    # col保存的是Queue在每一行的列号
    col = [0] * n

    def dfs(r, s):
        # s表示每一行可选列的集合
        if r == n:
            ans.append(['.'*c + 'Q' + '.'*(n-1-c) for c in col])
            return

        for c in s:
            if all(r+c != R+col[R] and r-c != R-col[R] for R in range(r)):
                col[r] = c
                dfs(r+1, s - {c})
    dfs(0, set(range(n)))
    return ans
