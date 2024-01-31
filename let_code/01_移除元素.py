"""
01_移除元素 - 
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组
Author: hanayo
Date： 2024/1/31
"""


def remove_ele(nums: list[int], val: int):
    """解法1：朴实无华的遍历"""
    i = 0
    # 注意此处，数组的长度是动态变化的，所以要在while条件里写i < len(nums)
    while i < len(nums):
        if val == nums[i]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


def rem_ele(nums: list[int], val: int):
    """解法2，双指针，将不重复的数，填充到本数组中"""
    i = j = 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1
    return j


if __name__ == '__main__':
    print(rem_ele([3, 2, 2, 3], 3))
