"""
哈希优化 - 

Author: hanayo
Date： 2024/2/22
"""


def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    """方法一：暴力枚举"""
    # 两层循环，时间复杂度为 O(n^2)
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[i] == target:
                return [i, j]
    return []


def two_sum_hash_table(nums: list[int], target: int) -> list[int]:
    """方法二：辅助哈希表"""
    # 辅助哈希表，空间复杂度为 O(n)
    dic = {}
    n = len(nums)
    for i in range(n):
        if target - nums[i] not in dic:
            dic[nums[i]] = i
        else:
            return [dic[target - nums[i]], i]
    return []
