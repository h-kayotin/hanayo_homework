"""
90_寻找两个正序数组的中位数 -

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

Author: hanayo
Date： 2024/6/20
"""
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    nums.sort()
    n = len(nums)
    if n % 2:
        idx = int(n // 2)
        return nums[idx]
    else:
        idx = n // 2
        return (nums[idx] + nums[idx-1]) /2



if __name__ == '__main__':
    find_median_sorted_arrays([1, 5], [3, 4])
    print(4 % 2)
    print(4 // 2)
    print(5 // 2)