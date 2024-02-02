"""
08_跳跃游戏 - 
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
Author: hanayo
Date： 2024/2/2
"""


def can_jump(nums: list[int]):
    max_place = 0
    end = len(nums) - 1
    for i, jump in enumerate(nums):
        # 最大步数大于i，表示当前步数是可以到达的
        if i < max_place < i + jump:
            max_place = i + jump
        if max_place < i:
            return False
    return max_place >= len(nums)


def can_jump2(nums: list[int]):

    pass


if __name__ == '__main__':
    my_nums = [2, 3, 1, 1, 4]
    print(can_jump(my_nums))
