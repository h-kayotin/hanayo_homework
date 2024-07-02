"""
111_前k个高频元素 - 

Author: hanayo
Date： 2024/7/2
"""
import heapq
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    num_dict = dict()
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    heap = []
    for key, val in num_dict.items():
        if len(heap) < k:
            heapq.heappush(heap, (val, key))
        else:
            if val > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (val, key))
    return [key for val, key in heap]


if __name__ == '__main__':
    print(top_k_frequent([1,1,1,2,2,3], 2))