"""
37_合并2个有序链表 - 

Author: hanayo
Date： 2024/4/15


"""
from typing import Optional


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next: ListNode | None = None


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]):
    cur = pre = ListNode(0)
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    cur.next = list1 if list1 else list2
    return pre.next
