"""
02_全排列问题 - 

Author: hanayo
Date： 2024/3/25
"""


def backtrack(
    state: list[int], choices: list[int], selected: list[bool], res: list[list[int]]
):
    """回溯算法：全排列 I"""
    # 当状态长度等于元素数量时，记录解
    if len(state) == len(choices):
        res.append(list(state))
    # 遍历所有选择
    for i, choice in enumerate(choices):
        # 剪枝，不允许重复元素
        if not selected[i]:
            # 尝试：做出选择，更新状态
            selected[i] = True
            state.append(choice)
            backtrack(state, choices, selected, res)
            # 回退：撤销选择，恢复到之前的状态
            selected[i] = False
            state.pop()


def permulations_i(nums: list[int]) -> list[list[int]]:
    """全排列"""
    res = []
    backtrack(state=[], choices=nums, selected=[False]*len(nums), res=res)
    return res


print(permulations_i([1, 2, 3]))
