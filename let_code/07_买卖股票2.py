"""
07_买卖股票2 - 
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。

Author: hanayo
Date： 2024/2/2
"""


# 这种算法事实上是不科学的，因为意味着提前预知了第二天股票是涨是跌
def max_profit(prices: list[int]):
    """买涨解法，只要涨就买"""
    max_money = 0
    for i in range(1, len(prices)):
        temp = prices[i] - prices[i-1]
        if temp > 0:
            max_money += temp
    return max_money


