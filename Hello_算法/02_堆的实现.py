"""
堆的实现 - 

Author: hanayo
Date： 2024/2/7
"""


class MyHeap:
    def __init__(self, nums: list[int]):
        self.max_heap = nums

    def peek(self) -> int:
        """访问堆顶元素"""
        return self.max_heap[0]

    @staticmethod
    def left(i: int) -> int:
        """获取左子节点的索引"""
        return 2 * i + 1

    @staticmethod
    def right(i: int) -> int:
        """获取右子节点的索引"""
        return 2 * i + 2

    @staticmethod
    def parent(i: int) -> int:
        """获取父节点的索引"""
        return (i - 1) // 2  # 向下整除

    def size(self):
        return len(self.max_heap)

    def swap(self, i, j):
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]

    def push(self, val: int):
        """元素入堆"""
        # 添加节点
        self.max_heap.append(val)
        # 从底至顶堆化
        self.sift_up(self.size() - 1)

    def sift_up(self, i: int):
        """从节点 i 开始，从底至顶堆化"""
        while True:
            # 获取节点 i 的父节点
            p = self.parent(i)
            # 当“越过根节点”或“节点无须修复”时，结束堆化
            if p < 0 or self.max_heap[i] <= self.max_heap[p]:
                break
            # 交换两节点
            self.swap(i, p)
            # 循环向上堆化
            i = p
