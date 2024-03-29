"""
02_贪心背包问题 - 

Author: hanayo
Date： 2024/3/29
"""


class Item:
    """物品"""

    def __init__(self, w: int, v: int):
        self.w = w  # 物品重量
        self.v = v  # 物品价值


def fractional_knapsack(wgt: list[int], val: list[int], cap: int) -> int:
    """分数背包：贪心"""
    # 创建物品列表，包含两个属性：重量、价值
    items = [Item(w, v) for w, v in zip(wgt, val)]
    # 按单位价值从大到小排序
    items.sort(key=lambda item: item.v / item.w, reverse=True)
    # 循环贪心选择
    res = 0
    # 遍历每个物品
    for item in items:
        # 放得下就放
        if item.w <= cap:
            res += item.v
            cap -= item.w
        # 放不下就切开放
        else:
            res += (item.v/item.w)*cap
            # 没空间了所以跳出循环
            break
    return res

