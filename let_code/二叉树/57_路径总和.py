"""
57_路径总和 - 

给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

Author: hanayo
Date： 2024/5/7
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: TreeNode, targetSum:int):
    def dfs(node: TreeNode, sum_list):
        if root is None:
            return 0
        sum_list = [num + node.val for num in sum_list] + [root.val]

        count = 0
        for num in sum_list:
            if num == targetSum:
                count += 1
        # count = sum_list.count(sum)

        return count + dfs(root.left, sum_list) + dfs(root.right, sum_list)

    return dfs(root, [])
