"""
33_二叉树中序遍历 - 

Author: hanayo
Date： 2024/4/12
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


res = []


def in_order(root: TreeNode| None):
    if root is None:
        return
    in_order(root.left)
    res.append(root.val)
    in_order(root.right)
