"""
54_二叉树展开为链表 - 

Author: hanayo
Date： 2024/4/29
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        前序遍历，递归
        """
        def dfs(node: Optional[TreeNode], pre: Optional[TreeNode]):
            if node is None:
                return
            pre = dfs(node.left, pre)
            pre = dfs(node.right, pre)

            node.right = pre
            node.left = None
            return node

        dfs(root, None)