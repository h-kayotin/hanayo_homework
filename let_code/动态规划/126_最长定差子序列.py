"""
126_最长定差子序列 - 
输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。
Author: hanayo
Date： 2024/7/17
"""
import collections
from typing import List


def longest_subsequence2(self, arr: List[int], difference: int) -> int:
    dp = dict()
    for num in arr:
        if num - difference in dp:
            dp[num] = dp[num-difference] + 1
        else:
            dp[num] = 1
    return max(dp.values())
