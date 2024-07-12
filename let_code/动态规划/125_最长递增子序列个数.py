"""
125_最长递增子序列个数 - 



Author: hanayo
Date： 2024/7/12
"""
from typing import List


def findNumberOfLIS(self, nums: List[int]) -> int:
    """
    f[i]表示i结尾的最长子序列长度，
    g[i]表示i结尾的最长子序列个数
    :param self:
    :param nums:
    :return:
    """
    n = len(nums)
    f = [1] * n
    g = [1] * n
    max_l = 1
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if f[i] < f[j] + 1:
                    f[i] = f[j] + 1
                    g[i] = g[j]
                elif f[i] == f[j] + 1:
                    g[i] += g[j]
        max_l = max(max_l, f[i])
    ans = 0
    for i in range(n):
        if f[i] == max_l:
            ans += g[i]
    return ans
