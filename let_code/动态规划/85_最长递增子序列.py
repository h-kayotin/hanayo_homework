"""
85_最长递增子序列 -
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
子序列
。

Author: hanayo
Date： 2024/6/13
"""
from typing import List


"""
解法2思路：
tails[k] 的值代表 长度为 k+1k+1k+1 子序列 的尾部元素值

比如序列是78912345，前三个遍历完以后tail是789，这时候遍历到1，就得把1放到合适的位置，于是在tail二分查找1的位置，
变成了189（如果序列在此时结束，因为res不变，所以依旧输出3），再遍历到2成为129，然后是123直到12345

"""


def length_of_lis(self, nums: List[int]) -> int:
    """动态规划"""
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def length_of_lis2(self, nums: List[int]) -> int:
    """动态规划，二分查找优化"""
    tails, res = [0] * len(nums), 0
    for num in nums:
        i, j = 0, res
        while i < j:
            m = (i + j) // 2
            if tails[m] < num:
                i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
            else:
                j = m
        tails[i] = num
        if j == res: res += 1
    return res


