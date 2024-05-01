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
                return pre
            pre = dfs(node.right, pre)
            pre = dfs(node.left, pre)

            node.right = pre
            node.left = None
            return node

        dfs(root, None)


def flatten(self, root: Optional[TreeNode]) -> None:
    """迭代"""
    while root:
        if root.left:
            sub_left = root.left
            # 找到当前左子树的最深的右子树
            while sub_left.right:
                sub_left = sub_left.right
            # 将root的右子树，挂在找到的左子树的最深右子树
            sub_left.right = root.right
            # 将root的左子树挂到右子树
            root.right = root.left
            # 清空左子树
            root.left = None
        root = root.right
