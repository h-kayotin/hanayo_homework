"""
01_二叉树遍历 - 

Author: hanayo
Date： 2024/3/25
"""


class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int):
        self.val: int = val                # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用


res = []


def pre_order(root: TreeNode):
    """前序遍历"""
    if root is None:
        return
    if root.val == 7:
        res.append(root)
    pre_order(root.left)
    pre_order(root.right)


path = list()


def pre_order2(root: TreeNode):
    """例题2"""
    if root is None:
        return
    # 尝试
    path.append(root)
    if root.val == 7:
        # 记录解
        res.append(list(path))
    pre_order(root.left)
    pre_order(root.right)
    # 回退
    path.pop()


def pre_order3(root: TreeNode):
    """例题3"""
    if root is None or root.val == 3:
        return
    # 尝试
    path.append(root)
    if root.val == 7:
        # 记录解
        res.append(list(path))
    pre_order(root.left)
    pre_order(root.right)
    # 回退
    path.pop()