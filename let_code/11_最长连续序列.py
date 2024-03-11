"""
11_最长连续序列 - 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

Author: kayotin
Date 2024/3/11
"""
import collections


def long_set(nums):
    num_set = set(nums)
    max_l = 0
    for num in nums:
        if num - 1 not in num_set:
            max_this = 1
            while num+1 in num_set:
                max_this += 1
                num += 1

            max_l = max(max_l, max_this)
    return max_l


if __name__ == '__main__':
    my_nums = [100, 4, 200, 1, 3, 2]

    print(long_set(my_nums))
