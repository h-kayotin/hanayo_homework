"""
102_多数元素 - 

给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

Author: hanayo
Date： 2024/6/27
"""
from typing import List


def majority_element(self, nums: List[int]) -> int:
    """哈希表统计法"""
    n = len(nums)
    ma_dict = dict()
    for num in set(nums):
        ma_dict[num] = 1
    for i in range(n):
        ma_dict[nums[i]] += 1
    new_dict = sorted(ma_dict, key=ma_dict.get, reverse=True)
    return new_dict[0]


def majority_element2(self, nums: List[int]) -> int:
    """数组排序法"""
    nums.sort()
    return nums[int(len(nums)/2)]


def majority_element3(self, nums: List[int]) -> int:
    """摩尔投票法"""
    votes = 0
    for num in nums:
        if votes == 0:
            x = num
        if num == x:
            votes += 1
        else:
            votes -= 1
    return x
