"""
堆 - 

Author: hanayo
Date： 2024/2/7
"""
import heapq

# 用列表创建小顶堆，python的堆默认是小顶堆
min_heap: list[int] = [1, 3, 2, 5, 4]
heapq.heapify(min_heap)

# 堆顶元素出堆
print(heapq.heappop(min_heap))
print(heapq.heappop(min_heap))
print(heapq.heappop(min_heap))
print(heapq.heappop(min_heap))
print(heapq.heappop(min_heap))

# 用flag*-1的方式创建大顶堆
vals = [1, 3, 2, 5, 4]
print(vals, "vals", type(vals))
max_heap = []
flag = -1

for num in vals:
    heapq.heappush(max_heap, flag*num)

# 获取栈顶元素
peek = flag * max_heap[0]
print("栈顶元素", peek)
print(type(max_heap), min_heap)

# 出堆
print(flag * heapq.heappop(max_heap))
print(flag * heapq.heappop(max_heap))
print(flag * heapq.heappop(max_heap))
print(flag * heapq.heappop(max_heap))
print(flag * heapq.heappop(max_heap))

