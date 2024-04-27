"""
50_二叉搜索树 - 

给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵
平衡
 二叉搜索树。

Author: kayotin
Date 2024/4/27
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_BST(nums: list[int]) -> Optional[TreeNode]:

    return build(nums, 0, len(nums)-1)


def build(nums, l, r):
    """递归分治"""
    if l > r:
        return None
    mid = int((l+r)/2)
    ans = TreeNode(nums[mid])
    ans.left = build(nums, l, mid-1)
    ans.right = build(nums, mid+1, r)
    return ans

