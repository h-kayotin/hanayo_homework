"""
02_容量蓄水问题 - 输入一个数组 ht ，其中的每个元素代表一个垂直隔板的高度。数组中的任意两个隔板，
以及它们之间的空间可以组成一个容器。请在数组中选择2个隔板，返回最大容量。

Author: hanayo
Date： 2024/3/29
"""


def max_capacity(ht: list[int]) -> int:
    """最大容量：贪心"""
    # 初始化 i, j，使其分列数组两端
    i, j = 0, len(ht) - 1
    res = 0
    # 循环贪心选择，直到相遇
    while i < j:
        cap = min(ht[i], ht[j]) * (j-i)
        res = max(cap, res)
        # 向内移动隔板
        if ht[i] < ht[j]:
            i += 1
        else:
            j -= 1
    return res
