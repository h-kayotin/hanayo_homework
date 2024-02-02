"""
06_买卖股票 - 
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

Author: hanayo
Date： 2024/2/2
"""


def max_profit(prices: list[int]):
    """解法1：最低买进，最高卖出，这是最优解法"""
    min_price = prices[0]
    max_money = 0
    for price in prices:
        min_price = min(min_price, price)
        max_money = max(max_money, price - min_price)
    return max_money


def max_profit2(prices: list[int]):
    n = len(prices)
    dp = [0] * n
    min_price = prices[0]

    for i in range(1, n):
        min_price = min(min_price, prices[i])
        dp[i] = max(dp[i-1], prices[i] - min_price)

    return dp[-1]

if __name__ == '__main__':
    my_prices = [7, 1, 5, 3, 6, 4]
    money = max_profit(my_prices)
    print(money)
