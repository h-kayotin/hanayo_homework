"""
14_接雨水 - 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

Author: hanayo
Date： 2024/3/15
"""


def trap(height: list[int]) -> int:
    waters = 0
    left = 0
    right = len(height) - 1
    left_max, right_max = 0, 0

    while left < right:
        # 每轮循环更新左边的最高高度和右边的最高高度
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        # 如果左边当前高度较低，计算左侧水池，左指针向右推进
        if height[left] < height[right]:
            waters += left_max - height[left]
            left += 1
        else:  # 否则，计算右侧水池，右指针向左推进
            waters += right_max - height[right]
            right -= 1

    return waters
