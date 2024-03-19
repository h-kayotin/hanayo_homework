"""
07_购物车问题 - 如何购买达到最大满意度？

先读懂背包问题：https://blog.csdn.net/bohu83/article/details/91453227

问题描述：有一个背包可以装物品的总重量为m，现有N个物品，每个物品重量是w[i]，价值v[i]，用背包装物品，能装的最大价值是多少？
Author: kayotin
Date 2024/3/19
"""


def max_bag(n: int, m: int, weight: list[int], prices: list[int]):
    """
    背包问题
    :param n: 可选物品总数量，矩阵的行
    :param m: 背包总重量，矩阵的列
    :param weight: 物品重量列表
    :param prices: 物品价格列表
    :return: 返回最大价值
    """
    res = [[0] * m for _ in range(n)]

    # 第一行
    for j in range(m):
        if j + 1 - weight[0] >= 0:
            res[0][j] = prices[0]
        else:
            res[0][j] = 0

    for i in range(1, n):
        for j in range(m):
            if j + 1 - weight[i] >= 0:
                res[i][j] = max(res[i-1][j], res[i-1][j+1-weight[i]] + prices[i-1])
            else:
                res[i][j] = res[i-1][j]
    return res[n-1][m-1]


my_n = 3
my_m = 4
my_weights = [1, 3, 4]
my_prices = [1500, 2000, 3000]
print(max_bag(my_n, my_m, my_weights, my_prices))






def max_cart():
    # 总预算
    money = 1000
    # 最多购买n件商品
    n = 5
    # 各商品价格,重要性如, q=0表示该商品可以单独购买，否则，需要购买前置物品 p - 1
    goods = [
        [800, 2, 0],
        [400, 5, 1],
        [300, 5, 1],
        [400, 3, 0],
        [500, 2, 0]
    ]

