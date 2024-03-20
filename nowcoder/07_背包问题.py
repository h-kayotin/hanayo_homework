"""
07_背包问题

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
            # 大于零说明装了当前商品之后还有空位，那么最大值就是在res[i-1][j]和
            #  当前价值prices[i] + 剩余格子价值
            # 这两者之间取最大值
            if j + 1 - weight[i] > 0:
                res[i][j] = max(res[i-1][j],  prices[i] + res[i-1][j+1-weight[i]])
            # 等于0，说明刚好能装这一个物品，所以最大值是要么上一行的这个格子，要么就是当前商品价值
            elif j + 1 - weight[i] == 0:
                res[i][j] = max(res[i - 1][j], prices[i])
            # 如果小于0，那就还是取上一行的
            else:
                res[i][j] = res[i-1][j]
    print(res)
    return res[n-1][m-1]


my_n = 3
my_m = 4
my_weights = [1, 4, 3]
my_prices = [1500, 3000, 2000]
print(max_bag(my_n, my_m, my_weights, my_prices))




