"""
04_返回多数元素 - 
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
Author: hanayo
Date： 2024/1/31
"""


def majority_num(nums):
    """哈希表统计法"""
    res_dict = dict()
    for num in nums:
        if num not in res_dict.keys():
            res_dict[num] = 1
        else:
            res_dict[num] += 1
    print(res_dict)

    res_list = sorted(res_dict, key=res_dict.get, reverse=True)
    print(res_list)
    return res_list[0]


def maj_num(nums: list[int]):
    """数组排序法。数组中心一定是众数"""
    new_list = nums
    new_list.sort()
    return new_list[int(len(new_list)/2)]


def mole_num(nums: list[int]):
    """摩尔投票法"""
    votes = 0
    x = 0
    for num in nums:
        if votes == 0:
            x = num
        if num == x:
            votes += 1
        else:
            votes -= 1
    return x


if __name__ == '__main__':
    my_nums = [1, 2, 2, 2, 3]
    print(mole_num(my_nums))