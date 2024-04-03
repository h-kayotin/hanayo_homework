"""
23_除自身以外数组的乘积 - 
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
Author: hanayo
Date： 2024/4/3
"""


"""
解题思路，上半区和下半区分开计算

1 2 3 4
1 1 3 4
1 2 1 4
1 2 3 1
b[0] = A[1] *A[2] * A[3] 
b[1] = A[0] * A[2] * A[3] 
...
"""


def product_except_self(nums: list[int]):
    n = len(nums)
    res = [1] * n
    # 计算左下半区
    for i in range(1, n):
        res[i] = res[i-1] * nums[i-1]
    # 计算右上半区
    tmp = 1
    for i in range(n-2, -1, -1):
        tmp *= nums[i+1]
        res[i] *= tmp
    return res

