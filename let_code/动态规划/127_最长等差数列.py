"""
127_最长等差数列 - 
给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。

Author: hanayo
Date： 2024/7/17
"""
from typing import List


def longest_arith_seq_length(self, nums: List[int]) -> int:
    """枚举公差"""
    n = len(nums)
    f = [[1] * 1001 for _ in range(n)]
    ans = 0
    for i in range(1, n):
        for k in range(i):
            j = nums[i] - nums[k] + 500
            f[i][j] = max(f[i][j], f[k][j] + 1)
            ans = max(ans, f[i][j])
    return ans



