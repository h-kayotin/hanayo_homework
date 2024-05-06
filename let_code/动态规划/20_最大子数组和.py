"""
20_最大子数组和 -
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

Author: hanayo
Date： 2024/4/1
"""


def max_sub_array(nums: list[int]):
    """贪心算法，某些情况下找不到最优解"""
    left, right = 0, len(nums) - 1
    sum_nums = sum(nums)
    while left < right:
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
        sum_nums = max(sum_nums,sum(nums[left: right + 1]))
    return sum_nums


def max_sub_array_dp(nums: list[int]):
    """动态规划法"""
    # dp[i]表示以nums[i]结尾的子数组的最大值
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        # 如果dp[i-1]小于0，那还不如取nums[i]
        dp[i] = max(dp[i-1] + nums[i], nums[i])
    return max(dp)


def max_sub_array_1(nums: list[int]):
    """动态规划，空间优化"""
    for i in range(1, len(nums)):
        nums[i] += max(nums[i-1], 0)
    return max(nums)


max_sub_array_dp([-2,1,-3,4,-1,2,1,-5,4])