"""
87_分割等和子集 - 
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
Author: hanayo
Date： 2024/6/17
"""
from typing import List


def can_partition(self, nums: List[int]) -> bool:
    sum_all = sum(nums)
    if sum_all % 2:
        return False
    target = sum_all // 2

    dp = [False] *(target+1)
    dp[0] = True
    # dp[i]表示 是否有和为i的子集
    for i in range(len(nums)):
        for j in range(target, nums[i]-1, -1):
            dp[j] = dp[j] or dp[j - nums[i]]
    return dp[-1]
