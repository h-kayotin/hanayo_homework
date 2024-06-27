"""
101_只出现一次的数字 - 

Author: hanayo
Date： 2024/6/27
"""
from typing import List


def single_number(self, nums: List[int]) -> int:
    """异或运算"""
    x = 0
    for num in nums:
        x ^= num
        print(x)
    return x
