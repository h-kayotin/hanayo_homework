"""
110_数组中第k个最大元素 - 

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

Author: hanayo
Date： 2024/7/2
"""
import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    nums.sort(reverse=True)
    return nums[k-1]


def find_kth_largest2(nums: List[int], k: int) -> int:
    """堆"""
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


if __name__ == '__main__':
    print(find_kth_largest2([3,2,1,5,6,4], 2))