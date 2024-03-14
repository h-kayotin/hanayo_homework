"""
12_移动0 - 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
Author: kayotin
Date 2024/3/14
"""


def move_zeros(nums: list[int]):
    if not nums:
        return
    n = len(nums)
    j = 0
    # 第一次循环，遇到不是0的，就和j交换，然后j+1
    for i in range(n):
        if nums[i]:
            nums[j] = nums[i]
            j += 1
    for i in range(j, n):
        nums[i] = 0


def move2(nums):
    if not nums:
        return
    n = len(nums)
    j = 0
    for i in range(n):
        # 只要遇到不是0的，就交换他和nums[j]的位置，j+1
        if nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1



if __name__ == '__main__':
    my_nums = [0, 0, 1, 0, 3, 12, 0]
    move2(my_nums)
    print(my_nums)
