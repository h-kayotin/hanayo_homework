"""
39_删除链表倒数第n个节点 - 

Author: hanayo
Date： 2024/4/18
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next: ListNode | None = None


def remove_n_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """两次遍历，直到链表总长度后"""
    dummy = ListNode(0)
    dummy.next = head
    n_len = 0
    cur = head
    while cur:
        n_len += 1
        cur = cur.next

    n_idx = n_len - n

    if n_idx == 0:
        return head

    cur = head
    for _ in range(n_idx - 1):
        cur = cur.next

    if cur.next and cur.next.next:
        cur.next = cur.next.next
    else:
        cur.next = None

    return dummy.next


def remove_n_from_end2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """快慢指针"""
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, dummy

    for _ in range(n):
        fast = fast.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


class Solution:
    def __init__(self):
        self.count = 0

    def remove_n_from_end3(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """递归"""
        if not head:
            self.count = 0
            return head
        head.next = self.remove_n_from_end3(head.next, n)
        self.count += 1
        return head.next if self.count == n else head


