"""
44_合并升序链表 - 

Author: hanayo
Date： 2024/4/26
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists:list[Optional[ListNode]]):
    """借助堆实现"""
    import heapq
    dummy = ListNode(0)
    p = dummy
    head = []
    for i in range(len(lists)):
        if lists[i]:
            # 入堆
            heapq.heappush(head, (lists[i].val, i))
            lists[i] = lists[i].next

    while head:
        # 出堆
        val, idx = heapq.heappop(head)
        p.next = ListNode(val)
        p = p.next
        if lists[idx]:
            heapq.heappush(head, (lists[idx].val, idx))
            lists[idx] = lists[idx].next

    return dummy.next


class Solution:
    """借助合并2个有序链表，分治递归"""
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 把 list1 加到新链表中
                list1 = list1.next
            else:  # 注：相等的情况加哪个节点都是可以的
                cur.next = list2  # 把 list2 加到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2  # 拼接剩余链表
        return dummy.next

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists)
        if m == 0:
            return None
        if m == 1:
            return lists[0]
        left = self.mergeKLists(lists[:m//2])
        right = self.mergeKLists(lists[m//2:])
        return self.mergeTwoLists(left, right)
