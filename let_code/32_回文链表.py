"""
32_回文链表 - 

Author: hanayo
Date： 2024/4/12
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next: ListNode | None = None


def is_palindrome(head: ListNode) -> bool:
    """翻转数组法"""
    res_list = []
    while head:
        res_list.append(head.val)
        head = head.next
    if res_list == res_list[::-1]:
        return True
    else:
        return False


def is_palindrome2(head: ListNode) -> bool:
    """中点遍历法"""
    # 计算长度
    cur = head
    n = 0
    while cur:
        n += 1
        cur = cur.next

    # 翻转前半部分链表
    pre = None
    cur = head
    i = 0
    while n // 2 != i:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
        i += 1
    # 奇数的时候，中间的数要跳过
    if n % 2 == 1:
        cur = cur.next

    # 分别进行比较
    while cur and pre:
        if cur.val != pre.val:
            return False
        cur = cur.next
        pre = pre.next
    return True
