"""
20_滑动窗口最大值 - 

Author: kayotin
Date 2024/3/31
"""
import collections


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """暴力解法，会超时"""
    slide_window = []
    res = []
    for i in range(k):
        slide_window.append(nums[i])

    res.append(max(slide_window))

    for i in range(k, len(nums)):
        slide_window.pop(0)
        slide_window.append(nums[i])

        res.append(max(slide_window))
    return res


def max_sliding_window2(nums: list[int], k: int) -> list[int]:
    """单栈队列法，队列是非增序列，deque[0]是窗口最大值"""
    if not nums or k == 0:
        return []
    deque = collections.deque()
    # 初始窗口
    for i in range(k):
        # 首先删除队列中所有比nums[i]小的元素
        while deque and deque[-1] < nums[i]:
            deque.pop()
        # 然后添加nums[i]
        deque.append(nums[i])
    # print(deque)
    res = [deque[0]]
    # 滑动窗口
    for i in range(k, len(nums)):
        # 如果滑动时，去掉的元素刚好是队列里最大的元素
        if deque[0] == nums[i-k]:
            # 就把该元素左侧出队
            deque.popleft()
        # 如果nums[i]大于队列中的元素，循环出队
        while deque and deque[-1] < nums[i]:
            deque.pop()
        deque.append(nums[i])
        res.append(deque[0])
        # print(deque)
    return res


if __name__ == '__main__':
    my_nums = [1,3,-1,-3,5,3,6,7]
    print(max_sliding_window2(my_nums, 3))