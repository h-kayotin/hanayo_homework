"""
81_打家劫舍 - 

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

Author: hanayo
Date： 2024/6/6
"""
from typing import List


def rob(nums: List[int]) -> int:
    """
    2种情况
    1. dp[n+1] = dp[n]
    2.dp[n+1] = dn[n-1] + nums[n]
    :param nums:
    :return:
    """
    n = len(nums)
    dp = [0] * (n+1)
    dp[1] = nums[0]
    for i in range(2, n+1):
        dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
    return dp[n]


def rob2(nums: List[int]):
    """空间优化"""
    cur, pre = 0, 0
    for num in nums:
        cur, pre = max(pre + num, cur), cur

    return cur