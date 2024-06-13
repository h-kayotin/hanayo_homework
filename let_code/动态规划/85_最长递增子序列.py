"""
85_最长递增子序列 - 

Author: hanayo
Date： 2024/6/13
"""
from typing import List


"""
dp[i]表示从0到i的nums成员，最长递增子序列长度

lis保存递增序列
dp[i+1]有两种情况，
nums[i+1]>lis[-1],递增序列加一
nums[i+1]<=lis[-1],递增序列不变

还要判断，如果长度是1，更新最小值

"""


def length_of_lis(self, nums: List[int]) -> int:
    """动态规划"""
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)