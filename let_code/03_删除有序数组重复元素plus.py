"""
03_删除有序数组重复元素plus - 
在2的基础上，保留重复元素，让重复元素只出现2次

Author: hanayo
Date： 2024/1/31
"""


def rem_ele(nums: list[int]):
    slow, fast = 0, 0
    while fast < len(nums):
        if slow < 2 or nums[slow-2] != nums[fast]:
            if slow != fast:
                nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


def rem_ele_plus(nums, k):
    """扩展到保留k个相同的值"""
    u = 0
    for num in nums:
        if u < k or nums[u-k] != num:
            nums[u] = num
            u += 1
    return u


if __name__ == '__main__':
    my_nums = [1, 2, 2, 2, 3, 3, 4]
    rem_ele(my_nums)