"""
104_下一个排列 - 

题干的意思是：找出这个数组排序出的所有数中，刚好比当前数大的那个数

比如当前 nums = [1,2,3]。这个数是123，找出1，2，3这3个数字排序可能的所有数，排序后，比123大的那个数 也就是132

如果当前 nums = [3,2,1]。这就是1，2，3所有排序中最大的那个数，那么就返回1，2，3排序后所有数中最小的那个，也就是1，2，3 -> [1,2,3]

Author: hanayo
Date： 2024/6/28
"""
from typing import List


def next_permutation(self, nums: List[int]) -> None:
    """
    第一步，倒序遍历查找到第一个降序的元素。
    第二步，第二次倒序遍历找到第一个大于降序元素的元素
    第三步，对第一个降序元素之后升序排列
    :param self:
    :param nums:
    :return:
    """
    i = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i != 0:
        j = len(nums)-1
        while nums[j] <= nums[i-1]:
            j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]

    nums[i:] = sorted(nums[i:])