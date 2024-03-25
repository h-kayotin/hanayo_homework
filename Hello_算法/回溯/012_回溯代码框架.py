"""
012_回溯代码框架 - 

Author: hanayo
Date： 2024/3/25
"""


class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int):
        self.val: int = val                # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None  # 右子节点引用


def is_solution(state: list[TreeNode]):
    """判断当前状态是否为解"""
    return state and state[-1].val == 7


def record_solution(state: list[TreeNode], res: list[list[TreeNode]]):
    """记录解"""
    res.append(list(state))


def is_valid(state: list[TreeNode], choice: TreeNode) -> bool:
    """判断当前状态下，该选择是否合法"""
    return choice is not None and choice.val != 3


def make_choice(state: list[TreeNode], choice: TreeNode):
    """更新状态"""
    state.append(choice)


def undo_choice(state: list[TreeNode], choice: TreeNode):
    """回复状态"""
    state.pop()


def backtrack(state: list[TreeNode], choices: list[TreeNode], res: list[list[TreeNode]]):
    """例题3，框架解法"""
    # 检查是否为解
    if is_solution(state):
        # 记录解
        record_solution(state, res)
    # 遍历所有选择
    for choice in choices:
        # 剪枝：检查选择是否合法
        if is_valid(state, choice):
            # 尝试：做出选择，更新状态
            make_choice(state, choice)
            # 进行下一轮选择
            backtrack(state, [choice.left, choice.right], res)
            # 回退：撤销选择，恢复到之前的状态
            undo_choice(state, choice)


# def backtrack(state: State, choices: list[choice], res: list[state]):
#     """回溯算法框架"""
#     # 判断是否为解
#     if is_solution(state):
#         # 记录解
#         record_solution(state, res)
#         # 不再继续搜索
#         return
#     # 遍历所有选择
#     for choice in choices:
#         # 剪枝：判断选择是否合法
#         if is_valid(state, choice):
#             # 尝试：做出选择，更新状态
#             make_choice(state, choice)
#             backtrack(state, choices, res)
#             # 回退：撤销选择，恢复到之前的状态
#             undo_choice(state, choice)
