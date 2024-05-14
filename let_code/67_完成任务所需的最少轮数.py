"""
67_完成任务所需的最少轮数 - 
给你一个下标从 0 开始的整数数组 tasks ，其中 tasks[i] 表示任务的难度级别。在每一轮中，你可以完成 2 个或者 3 个 相同难度级别 的任务。

返回完成所有任务需要的 最少 轮数，如果无法完成所有任务，返回 -1 。
Author: hanayo
Date： 2024/5/14
"""
from collections import Counter


class Solution:
    def minimum_rounds(self, tasks: list[int]) -> int:
        """因为2+1就等于3了，所以不能完成的情况只有一种，就是只出现1次的任务"""
        task_dict = Counter(tasks)
        count = 0
        for val in task_dict.values():
            if val == 1:
                return -1
            if val % 3 == 0:
                count += val // 3
            else:
                # 3无法完成的任务，只多1轮就可以完成了。因为余数只可能是2
                count += (1 + val // 3)

        return count
