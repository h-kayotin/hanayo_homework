"""
15_合唱队问题 - 中间最高，左侧递增，右侧递减，这就是一个合格的合唱队
输入描述：
用例两行数据，第一行是同学的总数 N ，第二行是 N 位同学的身高，以空格隔开

输出描述：
最少需要几位同学出列
Author: hanayo
Date： 2024/3/22
"""
import bisect


def find_up_sub(nums):
    """寻找最长递增序列"""
    # 完全遍历，n^2
    n = len(nums)
    up_list = [1] * n
    for i in range(n):
        for ii in range(i):
            if nums[ii] < nums[i]:
                up_list[i] = max(up_list[i], up_list[ii] + 1)
    return up_list


def up_sub2(nums):
    # 用二分查找，加快了速度
    n = len(nums)
    dp = [1] * n
    arr = [nums[0]]
    for i in range(1, n):
        if nums[i] > arr[-1]:
            arr.append(nums[i])
            dp[i] = len(arr)
        else:
            # 用二分查找到arr中第一个比nums[i]大的元素的位置
            pos = bisect.bisect_left(arr, nums[i])
            arr[pos] = nums[i]
            dp[i] = pos + 1
        print(arr)
    return dp


while True:
    try:
        N = int(input())
        s = list(map(int, input().split()))
        left_s = up_sub2(s) # 从左至右
        right_s = up_sub2(s[::-1])[::-1] # 从右至左
        sum_s = [left_s[i]+right_s[i]-1 for i in range(len(s))] # 相加并减去重复计算
        print(str(N-max(sum_s)))
    except EOFError:
        break
