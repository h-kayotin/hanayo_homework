"""
24_缺失的第一个正数 - 

给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

Author: hanayo
Date： 2024/4/3
"""


def first_miss_int(nums: list[int]):
    """暴力解法"""
    res = [0] * (max(nums)+1)
    for num in nums:
        if num > 0:
            res[num] = 1
    print(res)
    for i in range(1, len(res)):
        if res[i] == 0:
            return i
    return len(res)


def first_miss_int2(nums: list[int]):
    """
    思路：结果只可能在1 - n+1之间
    因为：
    1 ： 要么 2 - n-1全都在，此时取1
    2：要么 1 - n全在，此时取 n+1

    :param nums:
    :return:
    """
    n = len(nums)
    hash_size = n + 1

    # 小于0 和 大于n+1的数字都是无用的，先排除掉
    for i in range(n):
        if nums[i] <= 0 or nums[i] >= hash_size:
            nums[i] = 0

    for i in range(n):
        if nums[i] % hash_size != 0:
            pos = (nums[i] % hash_size) - 1
            nums[pos] = (nums[pos] % hash_size) + hash_size
    print(nums)
    for i in range(n):
        if nums[i] < hash_size:
            return i+1
    return hash_size


def max_int(nums: list[int]):
    n = len(nums)
    res = [0] * (n+1)

    # 保证数组中的数字在应该在的位置
    for i in range(1, n+1):
        if 1 <= nums[i-1] < n+1:
            res[nums[i-1]] = nums[i-1]
    # 检查数组，没数字的就是结果
    for i in range(1, n+1):
        if res[i] == 0:
            return i
    return n + 1






max_int([3,4,-1,1])
