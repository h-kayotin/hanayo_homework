"""
34_环形链表 - 

Author: hanayo
Date： 2024/4/12
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next: ListNode | None = None


def has_cycle(head: ListNode):
    """集合法"""
    node_set = set()

    while head:
        if head in node_set:
            return True
        node_set.add(head)
        head = head.next
    return False


def has_cycle2(head: ListNode):
    """快慢指针追赶法"""
    fast = slow = head
    while fast and slow:
        if fast.next:
            fast = fast.next.next
        else:
            break
        if fast == slow:
            return True
        slow = slow.next
    return False
