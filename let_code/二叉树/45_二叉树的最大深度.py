"""
45_二叉树的最大深度 - 

Author: kayotin
Date 2024/4/27
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_dep(root: Optional[TreeNode]):
    """后续遍历"""
    if not root:
        return 0
    return max(max_dep(root.left), max_dep(root.right)) + 1


def max_depth(root: Optional[TreeNode]):
    """层序遍历bfs，借助队列"""
    if not root:
        return 0
    queue, res = [root], 0
    while queue:
        # 用tmp存储当前层的节点
        tmp = []
        for node in queue:
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        queue = tmp
        res += 1
    return res
