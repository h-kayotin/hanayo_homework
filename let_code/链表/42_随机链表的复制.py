"""
42_随机链表的复制 - 

Author: hanayo
Date： 2024/4/22
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: Optional[Node]):
    if not head:
        return
    node_dic = dict()

    # 第一次遍历，新建各个node节点
    cur = head
    while cur:
        node_dic[cur] = Node(cur.val)
        cur = cur.next

    # 第二次遍历,赋值next和random
    cur = head
    while cur:
        node_dic[cur].next = node_dic.get(cur.next)
        node_dic[cur].random = node_dic.get(cur.random)
    return node_dic[head]
