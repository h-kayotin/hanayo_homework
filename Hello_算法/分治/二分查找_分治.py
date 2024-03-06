"""
二分查找_分治 - 用分治实现二分查找

Author: kayotin
Date 2024/3/6
"""


def dfs(nums: list[int], target: int, i: int, j: int) -> int:
    """二分查找：问题 f(i, j)"""
    # 若区间为空，代表无目标元素，则返回 -1
    if i > j:
        return -1
    # 计算中间索引点m
    m = (i + j) // 2
    if nums[m] < target:
        # 递归子问题 target在[m+1,j]中
        return dfs(nums, target, m+1, j)
    elif target < nums[m]:
        # 递归子问题 target在[i, m-1]中
        return dfs(nums, target, i, m-1)
    else:
        return m


def binary_search(nums: list[int], target: int) -> int:
    """二分查找"""
    n = len(nums)
    # 在[0, n-1]中查找
    return dfs(nums, target, 0, n-1)
