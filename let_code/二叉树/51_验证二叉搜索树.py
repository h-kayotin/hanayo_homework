"""
51_验证二叉搜索树 - 

Author: kayotin
Date 2024/4/28
"""
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode], left=-inf, right=inf,) -> bool:
    """前序遍历，每次更新左右边界"""
    if root is None:
        return True
    x = root.val
    return left < x < right and is_valid_bst(root.left, left, x) and is_valid_bst(root.right, x, right)


class Solution:
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """中序遍历"""
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)


