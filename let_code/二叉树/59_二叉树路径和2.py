"""
59_二叉树路径和2 - 

Author: hanayo
Date： 2024/5/10
"""
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0
            # 左子树最长路径
            l_val = dfs(node.left)
            # 右子树最长路径
            r_val = dfs(node.right)
            nonlocal ans
            # 左子树最大路径+右子树最长路径+当前节点值，更新res
            ans = max(ans, l_val + r_val + node.val)
            # 可能是负值，所以和0取一个最大值
            return max(max(l_val, r_val) + node.val, 0)
        dfs(root)
        return ans
