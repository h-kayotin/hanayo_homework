"""
107_跳跃游戏 - 

Author: hanayo
Date： 2024/7/1
"""
from typing import List


def can_jump(self, nums: List[int]) -> bool:
    max_length = 0
    for i, jump in enumerate(nums):
        if i > max_length:
            return False
        max_length = max(max_length, i + jump)
        if max_length >= len(nums) - 1:
            return True
