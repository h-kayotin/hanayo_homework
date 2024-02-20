"""
03_数组表示二叉树 - 

Author: kayotin
Date 2024/2/20
"""


class TreeNode:
    """二叉树节点类"""

    def __init__(self, val: int):
        self.val: int = val  # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用


class ArrayBinaryTree:
    """数组表示下的二叉树类"""

    def __init__(self, arr: list[int | None]):
        """构造方法"""
        self._tree = list(arr)
        self.res = []

    def size(self) -> int:
        """列表容量"""
        return len(self._tree)

    def val(self, i: int) -> int | None:
        """获取索引为i节点的值"""
        if i < 0 or i > self.size():
            return None
        else:
            return self._tree[i]

    def left(self, i: int) -> int | None:
        """返回左子节点的索引"""
        return 2*i + 1

    def right(self, i: int) -> int | None:
        """返回右子节点的索引"""
        return 2*i + 2

    def parent(self, i: int) -> int | None:
        """返回父节点的索引"""
        return (i-1)//2

    def level_order(self) -> list[int]:
        """层序遍历"""
        self.res = []
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res

    def dfs(self, i: int, order: str):
        """深度优先遍历"""
        if self.val(i) is None:
            return
        # 前序遍历
        if order == "pre":
            self.res.append(self.val(i))
        self.dfs(self.left(i), order)
        # 中序遍历
        if order == "in":
            self.res.append(self.val(i))
        self.dfs(self.right(i), order)
        # 后序遍历
        if order == "post":
            self.res.append(self.val(i))

    def pre_order(self) -> list[int]:
        """前序遍历"""
        self.res = []
        self.dfs(0, "pre")
        return self.res

    def in_order(self) -> list[int]:
        """中序遍历"""
        self.res = []
        self.dfs(0, "in")
        return self.res

    def post_order(self) -> list[int]:
        """后序遍历"""
        self.res = []
        self.dfs(0, "post")
        return self.res

