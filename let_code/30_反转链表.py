"""
30_反转链表 - 

Author: hanayo
Date： 2024/4/9
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next: ListNode | None = None


def reverse_list(head: ListNode):
    """双指针"""
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


def reverse_list2(head: ListNode):
    """递归"""
    def recur(cur, pre):
        if not cur:
            return pre
        res = recur(cur.next, cur)
        cur.next = pre
        return res
    return recur(head, None)