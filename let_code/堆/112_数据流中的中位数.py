"""
112_数据流中的中位数 - 

Author: hanayo
Date： 2024/7/2
"""
import heapq


class MedianFinder:

    def __init__(self):
        self.heap_a = []
        self.heap_b = []

    def addNum(self, num: int) -> None:
        if len(self.heap_a) != len(self.heap_b):
            heapq.heappush(self.heap_a, num)
            heapq.heappush(self.heap_b, -heapq.heappop(self.heap_a))
        else:
            heapq.heappush(self.heap_b, -num)
            heapq.heappush(self.heap_a, -heapq.heappop(self.heap_b))

    def findMedian(self) -> float:
        if len(self.heap_a) != len(self.heap_b):
            return self.heap_a[0]
        else:
            return (self.heap_a[0] - self.heap_b[0]) / 2