"""
12_最多蓄水 - 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

Author: kayotin
Date 2024/3/14
"""


def max_area(height:list[int])-> int:
    i, j = 0, len(height) - 1
    res = 0
    while i < j:
        # 计算面积，取最大值
        res = max(res, (j-i)*min(height[i], height[j]))
        # 难点在于理解为什么要移动左右之中，较小的那个
        # 如果移动长的那个，那么height可能变小或不变，因为水桶最短变取决于最短边，也就是之前短的那一边
        # 如果移动短的那个，那么height是有变大的可能的
        # 所以，最终的指针移动是移动height[i]较小的那一边
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res
