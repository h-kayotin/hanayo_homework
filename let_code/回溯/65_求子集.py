"""
65_求子集 - 
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的
子集
（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
无重复元素
Author: hanayo
Date： 2024/5/13
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """选或者不选某个数"""
        ans = []
        path = []
        n = len(nums)

        def dfs(i: int):
            if i == n:
                ans.append(path.copy())
                return
            # 不选nums[i]，直接递归i+1
            dfs(i+1)

            # 选nums[i],path中加入nums[i],然后再递归i+1
            path.append(nums[i])
            dfs(i+1)
            path.pop()

        dfs(0)
        return ans


class Solution2:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i: int):
            ans.append(path.copy())
            if i == n:
                return
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    solu = Solution2()
    print(solu.subsets(nums))