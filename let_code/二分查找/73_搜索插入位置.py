"""
73_搜索插入位置 -

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

Author: hanayo
Date： 2024/5/20
"""
from typing import List


def search_insert(self, nums: List[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <=j:
        m = (i+j) // 2
        if nums[m] < target:
            i = m+1
        elif target < nums[m]:
            j = m-1
        else:
            return m
    return i
