"""
02_删除有序数组重复元素 - 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

Author: hanayo
Date： 2024/1/31
"""


def rem_ele(nums: list[int]):
    """解法1：双指针法"""
    a = b = 0
    while a < len(nums) - 1:
        if nums[a+1] != nums[b]:
            b += 1
            # 设置这个判断条件，可以避免无意义的移动
            if a+1 > b:
                nums[b] = nums[a+1]
        a += 1
    return b+1


if __name__ == '__main__':
    my_nums = [1, 2, 2, 3, 3, 4]
    rem_ele(my_nums)