"""
89_寻找旋转排序数组中的最小值 - 
https://www.bilibili.com/video/BV1QK411d76w
Author: hanayo
Date： 2024/6/18
"""
from typing import List


def find_min(self, nums: List[int]) -> int:
    # 开区间(-1, n-1)
    left, right = -1, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < nums[-1]:
            right = mid
        else:
            left = mid
    return nums[right]
