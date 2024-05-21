"""
75_二分查找左边界和右边界 - 

Author: hanayo
Date： 2024/5/21
"""
from typing import List


def search_range(self, nums: List[int], target: int) -> List[int]:
    i = search_insert(nums, target)
    if i == len(nums) or nums[i] != target:
        i = -1
    j = search_insert(nums, target + 1) - 1
    if j == -1 or nums[j] != target:
        j = -1
    return [i, j]


def search_insert(nums: List[int], target: int):
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m+1
        elif nums[m] > target:
            j = m-1
        else:
            j = m-1
    return i
