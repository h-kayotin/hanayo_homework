"""
17_和为k的子数组 - 
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
子数组是数组中元素的连续非空序列。

Author: kayotin
Date 2024/3/30
"""
import collections


def subarray_sum(nums: list[int], k: int) -> int:
    """暴力解法"""
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            sub_num = nums[i: j+1]
            if sum(sub_num) == k:
                count += 1
    return count


def subarray_sum2(nums: list[int], k: int) -> int:
    """前缀和"""
    count = 0
    n = len(nums)
    pre_sum = [0]

    # 求前缀和
    temp = 0
    for num in nums:
        temp += num
        pre_sum.append(temp)

    # 求和为k的连续子数组，
    for i in range(1, n+1):
        for j in range(i, n+1):
            # 前j个数字的和 减去前i个数字的和
            if pre_sum[j] - pre_sum[i-1] == k:
                count += 1
    return count


def subarray_sum3(nums: list[int], k: int) -> int:
    """前缀和，默认数组优化"""
    count = 0
    n = len(nums)
    pre_sum_dict = collections.defaultdict(int)
    pre_sum_dict[0] = 1

    pre_sum = 0
    for i in range(n):
        pre_sum += nums[i]
        # 如果pre_sum - k不存在，默认值字典会返回0
        count += pre_sum_dict[pre_sum - k]

        pre_sum_dict[pre_sum] += 1
    return count


if __name__ == '__main__':
    my_nums = [1, 2, 3]
    print(subarray_sum2(my_nums, 3))