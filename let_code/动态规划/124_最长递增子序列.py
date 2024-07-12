"""
124_最长递增子序列 - 

Author: hanayo
Date： 2024/7/12
"""
from typing import List


def lengthOfLIS(self, nums: List[int]) -> int:
    """
    dp[i]代表以nums[i]结尾的最长子序列长度；
    状态转移：
    遍历j， j在[0,i)中，如果nums[i]比nums[j]大，那么可以加1
    因此dp[i] = max(dp[i], dp[j] + 1)
    :param self:
    :param nums:
    :return:
    """
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)