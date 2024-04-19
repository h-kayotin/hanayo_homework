"""
40_两两交换链表中的节点 - 

Author: hanayo
Date： 2024/4/19
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next: ListNode | None = None


def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """模拟"""
    dummy = ListNode(0)
    dummy.next = head

    cur = dummy
    while cur.next and cur.next.next:
        tmp_a, tmp_b = cur.next, cur.next.next
        cur.next = tmp_b
        tmp_a.next = tmp_b.next
        tmp_b.next = tmp_a
        cur = cur.next.next

    return dummy.next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """递归"""
        if head is None or head.next is None:
            return head

        node1 = head
        node2 = head.next
        node3 = node2.next

        node1.next = self.swapPairs(node3)
        node2.next = node1

        return node2

