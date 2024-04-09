"""
41_杨辉三角 - 

Author: hanayo
Date： 2024/4/9
"""


def get_even_idx(n: int):
    """从第三行开始，在2 3 2 4位置出现偶数"""
    if n <= 2:
        return -1
    alt_list = [2, 3, 2, 4]
    return alt_list[(n - 3) % 4]


def generate_triangle(n):
    """生成杨辉三角"""
    triangle = [[1] * (2 * i + 1) for i in range(n)]
    # 从第二行开始，是因为前2行全是1
    for i in range(2, n):
        for j in range(1, 2 * i):
            tmp = 0
            if 0 <= j <= 2 * (i - 1):
                tmp += triangle[i - 1][j]
            if 0 <= j - 1 <= 2 * (i - 1):
                tmp += triangle[i - 1][j - 1]
            if 0 <= j - 2 <= 2 * (i - 1):
                tmp += triangle[i - 1][j - 2]
            triangle[i][j] = tmp

    return triangle


# 示例：生成5行的杨辉三角
rows = generate_triangle(5)
for row in rows:
    print(row)
