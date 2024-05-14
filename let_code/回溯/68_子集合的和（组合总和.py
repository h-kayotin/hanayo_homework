"""
68_子集合的和（组合总和 - 

Author: hanayo
Date： 2024/5/14
"""
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """选或者不选"""
    ans = []
    path = []

    def dfs(i: int, left: int):
        if left == 0:
            ans.append(path.copy())
        if i == len(candidates) or left < 0:
            return
        # 不选
        dfs(i+1, left)

        # 选
        path.append(candidates[i])
        dfs(i, left - candidates[i])
        path.pop()
    dfs(0, target)
    return ans


def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    """选或者不选，剪枝优化，对数字排序，在left < candidates[i]时就可以跳出递归"""
    ans = []
    path = []
    candidates.sort()

    def dfs(i: int, left: int):
        if left == 0:
            ans.append(path.copy())
        if i == len(candidates) or left < candidates[i]:
            return
        # 不选
        dfs(i+1, left)

        # 选
        path.append(candidates[i])
        dfs(i, left - candidates[i])
        path.pop()
    dfs(0, target)
    return ans
