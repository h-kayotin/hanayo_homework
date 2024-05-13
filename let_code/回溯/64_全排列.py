"""
64_全排列 - 
无重复元素的全排列问题

Author: hanayo
Date： 2024/5/13
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.backs_track(state=[], choices=nums, selected=[False]*len(nums), res=res)
        return res

    def backs_track(self, state: list[int], choices: list[int], selected: list[bool], res: list[list[int]]):
        # 当所有数字都被选择了，记录解
        if len(state) == len(choices):
            res.append(list(state))
        # 遍历所有选择
        for i, choice in enumerate(choices):
            if not selected[i]:
                selected[i] = True
                state.append(choice)
                self.backs_track(state, choices, selected, res)
                # 回退
                selected[i] = False
                state.pop()
