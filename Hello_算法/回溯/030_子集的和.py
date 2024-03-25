"""
030_子集的和 - 

Author: hanayo
Date： 2024/3/25
"""


def backtrack(
    state: list[int], target: int, total: int, choices: list[int], res: list[list[int]]
):
    """回溯算法：全排列 I"""
    # 当子集和等于目标时，记录解
    if total == target:
        res.append(list(state))
        return
    # 遍历所有选择
    for i in range(len(choices)):
        # 剪枝，去掉不符合条件的
        if total + choices[i] > target:
            continue
            # 尝试：做出选择，更新状态
        state.append(choices[i])
        backtrack(state, target, total, choices, res)
        # 回退：撤销选择，恢复到之前的状态
        state.pop()


def subset_sum_i_naive(nums: list[int], target: int) -> list[list[int]]:
    """求解子集的和，包含重复元素"""
    state = []
    total = 0
    res = []
    backtrack(state, target, total, nums, res)
    return res
