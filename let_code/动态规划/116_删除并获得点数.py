"""
116_删除并获得点数 - 
给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
Author: hanayo
Date： 2024/7/5
"""
import collections
from typing import List


def delete_and_earn(self, nums: List[int]) -> int:
    """ """
    nums_map = collections.Counter(nums)
    max_num = max(nums_map.keys())
    dp = [0] *(max_num+1)

    dp[1] = 1 * nums_map[1]
    for i in range(2, max_num+1):
        # 不选当前数字， vs  选当前数字
        dp[i] = max(dp[i-1], dp[i-2] + i*nums_map[i])

    return dp[-1]


def delete_and_earn2(self, nums: List[int]) -> int:
    """ 空间优化"""
    nums_map = collections.Counter(nums)
    max_num = max(nums_map.keys())
    one, two = 0, 1 * nums_map[1]
    for i in range(2, max_num+1):
        one, two = two, max(two, one + i*nums_map[i])
    return two


delete_and_earn(1, [2,2,3,3,3,4])