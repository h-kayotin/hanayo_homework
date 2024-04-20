"""
071_背包问题优化 - 

Author: kayotin
Date 2024/3/20
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
    # 建立一个 n+1 * m+1的矩阵，这样res[i][j]就代表：第i个物品在背包容量为j的时候的最优解
    res = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if j - weight[i-1] >=0:
                res[i][j] = max(res[i-1][j], prices[i-1] + res[i-1][j-weight[i-1]])
            else:
                res[i][j] = res[i-1][j]
    print(res)
    return res[n][m]


if __name__ == '__main__':
    my_n = 3
    my_m = 4
    my_weights = [1, 4, 3]
    my_prices = [1500, 3000, 2000]
    print(max_bag(my_n, my_m, my_weights, my_prices))