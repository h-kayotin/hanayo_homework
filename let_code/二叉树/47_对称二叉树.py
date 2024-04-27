"""
47_对称二叉树 - 
检查二叉树是否左右轴对称

Author: kayotin
Date 2024/4/27
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """递归判断每个节点"""
    def recur(l, r):
        if not l and not r:
            return True
        if not l or not r or l.val != r.val:
            return False
        return recur(l.left, r.right) and recur(l.right, r.left)
    return not root or recur(root.left, root.right)