"""
26_螺旋矩阵 - 

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

Author: hanayo
Date： 2024/4/4
"""


def spiral_order(matrix: list[list[int]]):
    """模拟"""
    if not matrix:
        return []
    left, top = 0, 0
    right, bottom = len(matrix[0])-1, len(matrix)-1
    res = []

    while True:
        # 右
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        if top > bottom:
            break

        # 下
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1
        if left > right:
            break

        # 左
        for i in range(right, left-1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1
        if top > bottom:
            break

        # 上
        for i in range(bottom, top-1, -1):
            res.append(matrix[i][left])
        left += 1
        if left>right:
            break
    return res


def spiral_matrix(matrix: list[list[int]]):
    """翻转矩阵法"""
    res = []
    while matrix:
        res += matrix.pop(0)
        # 解包，并纵向打包，然后反向，就实现了翻转
        matrix = list(zip(*matrix))[::-1]
    return res


my_ma = [[1,2,3],[4,5,6],[7,8,9]]
print(*(my_ma))
my_ma = list(zip(*my_ma))

print(my_ma)


