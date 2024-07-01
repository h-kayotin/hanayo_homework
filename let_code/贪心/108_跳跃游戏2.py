"""
108_跳跃游戏2 - 
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
Author: hanayo
Date： 2024/7/1
"""
from typing import List


def jump(self, nums: List[int]) -> int:
    """动态规划，不太好，可能需要n^2"""
    n = len(nums)
    dp = [i for i in range(n)]
    for i in range(2, n):
        steps = []
        for j in range(i):
            if nums[j] + j >= i:
                steps.append(dp[j]+1)
        dp[i] = min(steps)
    return dp[n-1]


def jump2(self, nums: List[int]) -> int:
    """贪心"""
    # end表示当前走到位置， max表示最远可以走到的位置
    end, max_pos = 0, 0
    steps = 0
    for i in range(len(nums)-1):
        # 每次更新最远可走到的距离
        max_pos = max(max_pos, nums[i] + i)
        # i表示走到该位置，那么更新可以走到的最远距离，并走一步
        if i == end:
            end = max_pos
            steps += 1
    return steps
