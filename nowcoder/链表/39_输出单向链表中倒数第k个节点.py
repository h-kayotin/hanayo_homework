"""
39_输出单向链表中倒数第k个节点 - 

Author: hanayo
Date： 2024/4/8
"""


class ListNode:
    """链表节点类"""

    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None


def gene_linked_list(num_list: list[int]):
    """输入数组，构成链表"""
    root = pre = ListNode(0)
    for num in num_list:
        root.next = ListNode(num)
        root = root.next
    return pre.next


def find_k(root: ListNode, k: int):
    """返回倒数第k个节点"""
    slow, fast = root, root
    for _ in range(k):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow.val


while True:
    try:
        n_len = input()
        num_list = [int(x) for x in str(input()).split()]
        k = int(input())
        head = gene_linked_list(num_list)
        print(find_k(head, k))
    except EOFError:
        break


