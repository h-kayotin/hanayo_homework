"""
86_乘积最大子数组 - 
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续
子数组
（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

Author: hanayo
Date： 2024/6/14
"""
from typing import List


def max_product(self, nums: List[int]) -> int:
    """
    当前的最大
    """
    if not nums:
        return 0
    res = nums[0]
    pre_max = pre_min = nums[0]
    for num in nums[1:]:
        cur_max = max(pre_max*num, pre_min*num, num)
        cur_min = min(pre_max*num, pre_min*num, num)
        res = max(res, cur_max)
        pre_max = cur_max
        pre_min = cur_min
    return res
