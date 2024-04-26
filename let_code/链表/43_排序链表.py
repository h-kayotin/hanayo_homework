"""
43_排序链表 - 

Author: hanayo
Date： 2024/4/25
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head: Optional[ListNode]):
    """列表排序法"""
    if not head:
        return None
    node_list = []
    cur = head
    while cur:
        node_list.append((cur, cur.val))
        cur = cur.next
    node_list.sort(key=lambda x:x[1])

    for i in range(len(node_list) - 1):
        node_list[i][0].next = node_list[i+1][0]
    node_list[-1][0].next = None
    return node_list[0][0]


def sort_list2(head: Optional[ListNode]):
    """递归，归并排序"""
    if not head or not head.next:
        return head

    # 从中间切分链表
    slow, fast = head, head.next
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    mid, slow.next = slow.next, None
    left, right = sort_list2(head), sort_list2(mid)

    # 合并左右链表
    h = res = ListNode(0)
    while left and right:
        if left.val < right.val:
            h.next, left = left, left.next
        else:
            h.next, right = right, right.next
        h = h.next
    h.next = left if left else right
    return res.next



