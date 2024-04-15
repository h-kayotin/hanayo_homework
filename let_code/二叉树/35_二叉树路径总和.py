"""
35_二叉树路径总和 -

给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，
这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

Author: hanayo
Date： 2024/4/13
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


def has_path_sum(root: TreeNode, targetSum: int) -> bool:
    """前序遍历，记录根到叶节点的值"""
    target =targetSum

    def is_leaf(node: TreeNode):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    res = []
    path = []
    tag = False

    def pre_order(node: TreeNode):
        if node is None:
            return
        path.append(node.val)
        if is_leaf(node):
            if sum(path) == target:
                res.append(sum(path))
                return
        pre_order(node.left)
        pre_order(node.right)
        path.pop()

    pre_order(root)
    if res:
        return True
    return False


def hasPathSum(root: TreeNode, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.val
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum-root.val)











