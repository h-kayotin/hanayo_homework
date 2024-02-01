"""
05_轮转数组 - 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

Author: hanayo
Date： 2024/2/1
"""


def rotate1(nums: list[int], k):
    """方法一：直接插入法"""
    if k := (k % len(nums)):
        for i in range(k):
            nums.insert(0, nums.pop())


def rotate2(nums: list[int], k):
    """方法2：数组切片法"""
    # 此处加if条件，是因为如何轮转次数刚好是数组长度的倍数，那么结果还是原数组
    if k := (k % len(nums)):
        k = k % len(nums)
        nums[:k], nums[k:] = nums[-k:], nums[:-k]


def rotate3(nums: list[int], k):
    """"""


if __name__ == '__main__':
    my_nums = [1, 2, 3, 4, 5]
    rotate2(my_nums, 7)
    print(my_nums)
