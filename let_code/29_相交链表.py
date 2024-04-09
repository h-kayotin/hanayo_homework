"""
29_相交链表 - 
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
Author: hanayo
Date： 2024/4/9
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node1(headA: ListNode, headB: ListNode):
    """暴力解法"""
    a = headA
    while a:
        b = headB
        while b:
            if a == b:
                return a.val
            b = b.next
        a = a.next
    return None


def get_intersection_node(headA: ListNode, headB: ListNode):
    """a + (b-c) = b + (a-c)法"""

    head_a, head_b = headA, headB
    while head_a != head_b:
        if head_a:
            head_a = head_a.next
        else:
            head_a = headB

        if head_b:
            head_b = head_b.next
        else:
            head_b = headA

    return head_a
