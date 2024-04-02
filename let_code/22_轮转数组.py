"""
22_轮转数组 - 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

Author: hanayo
Date： 2024/4/2
"""


def rotate(nums: list[int], k: int):
    n = len(nums)
    k = k % n
    return nums[-k:]+nums[:-k]


print(rotate([1,2,3,4,5,6,7], 3))
