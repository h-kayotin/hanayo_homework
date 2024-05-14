"""
68_子集合的和（组合总和 - 

Author: hanayo
Date： 2024/5/14
"""
from typing import List


class Solution1:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
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
