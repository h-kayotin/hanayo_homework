"""
01_爬楼梯 - 给定一个共有 n 阶的楼梯，你每步可以上
 1阶或者2  阶，请问有多少种方案可以爬到楼顶？

Author: hanayo
Date： 2024/3/25
"""


def backtrack(
    state: int, choices: list[int], n: int, res: list[int]
):
    """回溯算法：全排列 I"""
    # 当爬到顶时候，
    if state == n:
        res[0] += 1
    # 遍历所有选择
    for choice in choices:
        # 剪枝，不允许重复元素
        if state + choice > n:
            continue
        # 尝试：做出选择，更新状态
        backtrack(state + choice, choices, n, res)
        # 回退，因为state + choice在递归调用中，所以实际上还没加
        # 这里的回退相当于 state = state - choice


def climbing_stairs_backtrack(n: int) -> int:
    """爬楼梯：穷举回溯"""
    choices = [1, 2]
    state = 0
    res = [0]
    backtrack(state, choices, n, res)
    return res[0]
