"""
46_翻转二叉树 - 

Author: kayotin
Date 2024/4/27
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """递归"""
    if not root:
        return
    tmp = root.left
    root.left = invert_tree(root.right)
    root.right = invert_tree(tmp)

    return root


def invert_t(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """栈遍历所有节点，交换左右节点"""
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        node.left, node.right = node.right, node.left
    return root
