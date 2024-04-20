"""
35_数独 -

问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，推算出所有剩余空格的数字，
并且满足每一行、每一列、每一个3X3粗线宫内的数字均含1-9，并且不重复。


数据范围：输入一个 9*9 的矩阵
输入描述：
包含已知数字的9X9盘面数组[空缺位以数字0表示]

输出描述：
完整的9X9盘面数组

Author: hanayo
Date： 2024/4/4
"""


def check(board, x, y):
    """
    填入数字后，判断数独是否成立，
    :param board: 棋盘
    :param x: 填入数字的行
    :param y: 填入数字的列
    :return: 是否构成一个数独
    """
    # 验证y那一列，是否有相同数字
    for i in range(9):
        if i != x and board[i][y] == board[x][y]:
            return False
    # 验证x那一行，是否有相同数字
    for j in range(9):
        if j != y and board[x][j] == board[x][y]:
            return False
    # 验证填入数字的9宫格，是否有相同数字
    m, n = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if (i + m != x or j + n != y) and board[i + m][j + n] == board[x][y]:
                return False
    return True


def dfs(board: list[list[int]]):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # 在1到9中选一个数字
                for num in range(1, 10):
                    board[i][j] = num
                    if check(board, i, j) and dfs(board):
                        return True
                    # 回溯
                    board[i][j] = 0
                return False
    return True


matrix = []
for i in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)
dfs(matrix)
for i in range(9):
    matrix[i] = list(map(str, matrix[i]))
    print(" ".join(matrix[i]))
