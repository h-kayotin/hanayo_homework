"""
31_从前序遍历和中序遍历构造二叉树 - 

Author: kayotin
Date 2024/4/11
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: None | TreeNode = left
        self.right: None | TreeNode = right


def build_tree(preorder: list[int], inorder: list[int]):
    def recur(root, left, right):
        # 递归终止条件
        if left > right:
            return
        # 建立根节点
        node = TreeNode(preorder[root])
        # 划分根节点、左子树、右子树
        i = dic[preorder[root]]
        # 开启左子树递归
        node.left = recur(root+1, left, i-1)
        # 开启右子树递归
        node.right = recur(i-left+root+1, i+1, right)
        return node

    dic, preorder = {}, preorder
    for i in range(len(inorder)):
        dic[inorder[i]] = i
    return recur(0, 0, len(inorder) - 1)