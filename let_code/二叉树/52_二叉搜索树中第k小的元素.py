"""
52_二叉搜索树中第k小的元素 - 

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
    def __init__(self):
        self.k = 0
        self.res = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """实际上就是找中序遍历的第k个"""
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.right)

        self.k = k
        dfs(root)
        return self.res