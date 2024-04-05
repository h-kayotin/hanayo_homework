"""
34_迷宫问题 - 

Author: hanayo
Date： 2024/4/4
"""


def dfs(row, col):
    # 分别表示 左， 右， 上， 下
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 说明已经走到终点
    if row == m-1 and col == n-1:
        for res in path:
            print(f"({res[0]},{res[1]})")
        return

    # 每一步试探4个方向
    for idx in range(4):
        x = row + dx[idx]
        y = col + dy[idx]
        # 如果可以走，就继续往下走，把这一步标1，表示已走过
        if m > x >= 0 and 0 <= y < n and not matrix[x][y] == 1:

            matrix[x][y] = 1
            path.append((x, y))
            # 递归走下一个
            dfs(x, y)
            # 走不了就回头，在已走路径删除，并重新至0
            matrix[x][y] = 0
            path.pop()

    return


# m, n = [int(x) for x in str(input()).split(" ")]
# matrix = []
# for i in range(m):
#     m_row = [int(x) for x in str(input()).split(" ")]
#     matrix.append(m_row)
m, n = 5, 5
matrix = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
# 开始节点
path = [(0, 0)]
# 标位1表示这个点已经走过
matrix[0][0] = 1
dfs(0, 0)

