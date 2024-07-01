"""
105_寻找重复数 - 

Author: hanayo
Date： 2024/6/28
"""
from typing import List


def find_duplicate(self, nums: List[int]) -> int:
    """原地交换法"""
    i = 0
    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        if nums[nums[i]] == nums[i]:
            return nums[i]
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1


def find_duplicate2(self, nums: List[int]) -> int:
    """链表法，有重复就一定有环"""
    def next_val(i):
        return nums[i]

    slow = fast = 0

    # 第一次相遇
    while True:
        slow = next_val(slow)
        fast = next_val(next_val(fast))
        if slow == fast:
            break
    # 第二次相遇
    slow = 0
    while slow != fast:
        slow = next_val(slow)
        fast = next_val(fast)
    return slow
