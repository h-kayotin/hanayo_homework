"""
70_单词搜索 - 
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

Author: kayotin
Date 2024/5/19
"""
from typing import List


def exist(self, board: List[List[str]], word: str) -> bool:
    def dfs(i, j, k):
        # 递归边界，超过行或列最大值，或者和字符不匹配
        if not 0 <= i < len(board) or not 0 <=j < len(board[0]) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        board[i][j] = ''
        res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
        # 回溯
        board[i][j] = word[k]
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False
