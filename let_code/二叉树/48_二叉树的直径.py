"""
48_二叉树的直径 - 
给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

Author: kayotin
Date 2024/4/27
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binarytree(root: Optional[TreeNode]) -> int:
    """递归"""
    ans = 0

    def dfs(node: Optional[TreeNode]):
        if node is None:
            return -1
        l_length = dfs(node.left) + 1
        r_length = dfs(node.right) + 1
        nonlocal ans
        ans = max(ans, l_length+r_length)
        return max(l_length, r_length)
    dfs(root)
    return ans
