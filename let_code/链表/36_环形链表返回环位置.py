"""
36_环形链表返回环位置 - 
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
Author: hanayo
Date： 2024/4/15
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next: ListNode | None = None


def detect_cycle(head: ListNode):
    """集合法"""
    node_set = set()

    while head:
        if head in node_set:
            return head
        node_set.add(head)
        head = head.next
    return None


def detect_cycle2(head: ListNode):
    """快慢指针"""
    fast = slow = head
    while True:
        if not(fast and fast.next):
            return
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast

