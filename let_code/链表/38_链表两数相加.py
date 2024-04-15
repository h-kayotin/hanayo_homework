"""
38_链表两数相加 - 

Author: hanayo
Date： 2024/4/15
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next: ListNode | None = None


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """模拟"""
    carry = 0
    cur = res = ListNode(0)

    while l1 or l2 or carry:
        carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        # 存储小于10的部分
        cur.next = ListNode(carry % 10)
        # 保留大于10的部分
        carry //= 10
        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return res.next


def add_two_numbers2(l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
    """递归"""
    if l1 is None and l2 is None:
        return ListNode(carry) if carry else None
    if l1 is None:
        l1, l2 = l2, l1

    carry += l1.val + (l2.val if l2 else 0)
    l1.val = carry % 10
    l1.next = add_two_numbers2(l1.next, l2.next if l2 else None, carry // 10)
    return l1
