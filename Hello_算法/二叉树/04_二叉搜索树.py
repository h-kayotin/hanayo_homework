"""
04_二叉搜索树 - 

Author: kayotin
Date 2024/2/20
"""


class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int):
        self.val: int = val                # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用


class BinarySearchTree:
    """二叉搜索树"""
    def __init__(self):
        self._root = None

    def search(self, num: int) -> TreeNode | None:
        """查找节点"""
        cur: TreeNode = self._root
        while cur is not None:
            # 当前值小于目标，说明目标在右子树
            if cur.val < num:
                cur = cur.right
            # 目标小于当前值，说明目标在左子树
            elif num < cur.val:
                cur = cur.left
            else:
                break
        return cur

    def insert(self, num: int):
        """插入节点"""
        # 若树为空，则初始化根节点,也就是直接插在根节点
        if self._root is None:
            self._root = TreeNode(num)
            return
        # 循环插找
        cur, pre = self._root, None
        while cur is not None:
            # 找到重复值，直接return
            if cur.val == num:
                return
            pre = cur
            if cur.val < num:
                cur = cur.right
            else:
                cur = cur.left
        # 插入节点
        node = TreeNode(num)
        if pre.val < num:
            pre.right = node
        else:
            pre.left = node

    def remove(self, num: int):
        """删除节点"""
        # 若树为空，直接提前返回
        if self._root is None:
            return
        # 循环查找，越过叶节点后跳出
        cur, pre = self._root, None
        while cur is not None:
            # 找到要删除的值，跳出循环
            if cur.val == num:
                break
            pre = cur
            if cur.val < num:
                cur = cur.right
            else:
                cur = cur.left
        # 如果没找到要删除的节点，直接返回
        if cur is None:
            return
        # 有0个或1个子节点
        if cur.left is None or cur.right is None:
            child = cur.left or cur.right
            if cur != self._root:
                if pre.left == cur:
                    pre.left = child
                else:
                    pre.right = child
            else:
                # 如果删除的是根节点，重新指定根节点
                self._root = child
        # 有2个子节点
        else:
            temp: TreeNode = cur.right
            while temp.left is not None:
                temp = temp.left
                self.remove(temp.val)
            cur.val = temp.val

