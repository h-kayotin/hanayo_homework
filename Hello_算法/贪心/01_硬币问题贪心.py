"""
01_硬币问题贪心 - 

Author: hanayo
Date： 2024/3/29
"""


def coin_change_greedy(coins: list[int], amt: int) -> int:
    """零钱兑换：贪心"""
    # 假设 coins 列表有序
    i = len(coins) - 1
    count = 0
    # 循环选择硬币，直到金额为0
    while amt > 0:
        # 每次选择小于金额的最大硬币面额
        while i > 0 and coins[i] > amt:
            i -= 1
        amt -= coins[i]
        count += 1
    return count if amt == 0 else -1
