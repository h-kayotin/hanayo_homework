"""
55_雇佣k位工人的总代价 - 

Author: hanayo
Date： 2024/5/1
"""

import heapq
from heapq import heapify


def total_cost(self, costs: list[int], k: int, candidates: int) -> int:
    # 必定能取到前k个最小的元素，直接返回他们的和即可
    n = len(costs)
    if candidates*2 + k > n:
        costs.sort()
        return sum(costs[:k])

    # 初始化堆
    l_heap = costs[: candidates]
    r_heap = costs[-candidates:]
    heapify(l_heap)
    heapify(r_heap)

    # 每次执行比较，左右堆中较小的出堆，然后通过下标补充进堆
    ans = 0
    i = candidates
    j = n - 1 - candidates
    for _ in range(k):
        if l_heap[0] < r_heap[0]:
            ans += heapq.heapreplace(l_heap, costs[i])
            i += 1
        else:
            ans += heapq.heapreplace(r_heap, costs[j])
            j -= 1
    return ans
