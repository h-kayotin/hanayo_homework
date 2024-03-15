"""
13_三数之和 - 在nums中，找出所有三个数和为0的组合。

Author: hanayo
Date： 2024/3/15
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    if not nums or n < 3:
        return []
    nums.sort()

    res = []
    for i in range(n):
        # 已经排序过的数组，只可能在右边找结果，所以nums[i]大于0就可以结束了
        if nums[i] > 0:
            return res
        # 重复数字跳过
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right -1]:
                    right -= 1
                left += 1
                right -= 1
            # 小于0，说明需要数字大一点，左指针往右移动
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            # 反之，如果和大于0，说明需要小一点，那么向左移动
            else:
                right -= 1
    return res



