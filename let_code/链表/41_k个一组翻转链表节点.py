"""
41_k个一组翻转链表节点 - 

Author: kayotin
Date 2024/4/20
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 计算链表长度
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        p0 = dummy = ListNode(next=head)
        pre = None
        cur = head
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next
            nxt.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next


def reverse_k(head: Optional[ListNode], k: int):
    """借助栈翻转"""
    h = t = ListNode(0, head)
    p, stack = head, []
    while True:
        for _ in range(k):
            # 每次k个元素入栈
            if p:
                stack.append(p)
                p = p.next
            # 数量不满7个，return
            else:
                return p.next
        # 进行翻转
        for _ in range(k):
            t.next = stack.pop()
            t = t.next
        # 继续做下一个k
        t.next = p
