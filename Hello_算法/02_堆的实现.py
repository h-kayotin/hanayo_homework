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
        """获取堆的大小"""
        return len(self.max_heap)

    def is_empty(self):
        """判断堆是否为空"""
        return self.size()

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

    def pop(self) -> int:
        """元素出堆"""
        # 判空处理
        if self.is_empty():
            raise IndexError("堆为空")
        # 交换根节点与最右叶节点（交换首元素与尾元素）
        self.swap(0, self.size() - 1)
        # 删除节点
        val = self.max_heap.pop()
        # 从顶至底堆化
        self.sift_down(0)
        # 返回堆顶元素
        return val

    def sift_down(self, i: int):
        """从节点i开始，从顶至底堆化"""
        while True:
            # 在左节点、右节点、当前节点中，找出最大的节点
            l, r, ma = self.left(i), self.right(i), i
            if l < self.size() and self.max_heap[l] > self.max_heap[ma]:
                ma = l
            if r < self.size() and self.max_heap[r] > self.max_heap[ma]:
                ma = r
            # 如果节点i已经是最大的了，或者lr越界，就跳出循环
            if ma == i:
                break
            # 交换节点的值
            self.swap(i, ma)
            # 向下推进
            i = ma
