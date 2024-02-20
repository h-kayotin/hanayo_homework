"""
03_建堆 - 

Author: kayotin
Date 2024/2/19
"""

import heapq


def top_k_heap(nums: list[int], k: int) -> list[int]:
    # 初始化小顶堆
    heap = []
    # 将前k个元素入堆
    for i in range(k):
        heapq.heappush(heap, nums[i])
    # 从第k+1个元素开始，保持堆的长度是k
    for i in range(k, len(nums)):
        # 如果当前元素大于堆顶元素，将堆顶元素出堆，将该元素入堆
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    return heap


if __name__ == '__main__':
    my_nums = [1, 3, 2, 4, 4, 5]
    print(top_k_heap(my_nums, 4))
