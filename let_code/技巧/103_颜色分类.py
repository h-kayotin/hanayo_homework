"""
103_颜色分类 - 
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。
Author: hanayo
Date： 2024/6/28
"""
from typing import List


def sort_colors(self, nums: List[int]) -> None:
    def swap(nums_list, index1, index2):
        nums_list[index1], nums[index2] = nums_list[index2], nums[index1]

    n = len(nums)
    if n < 2:
        return

    zero = 0
    two = n
    i = 0
    while i < two:
        if nums[i] == 0:
            swap(nums, i, zero)
            i += 1
            zero += 1
        elif nums[i] == 1:
            i += 1
        else:
            two -= 1
            swap(nums, i, two)