"""
37_删除单向链表中指定值节点 - 

Author: kayotin
Date 2024/4/6
"""


class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None


def find(head: ListNode, target: int):
    while head:
        if head.val == target:
            return head
        else:
            head = head.next
    return False


input_list = [int(x) for x in str(input()).split()]
n_len = input_list[0]
root = ListNode(input_list[1])
op_list = input_list[2:]

# 构造链表
for i in range(0, (n_len-1)*2, 2):
    node = ListNode(op_list[i])
    pre_node = find(root, op_list[i+1])
    if pre_node.next:
        node.next = pre_node.next
    pre_node.next = node

# 删除指定节点
del_node = op_list[-1]

# 删除节点
s_root = ListNode(0)
s_root.next = root
node = s_root
while node.next:
    if node.next.val == del_node:
        node.next = node.next.next
    node = node.next

# 打印
while s_root.next:
    print(s_root.next.val, end=" ")
    s_root = s_root.next

