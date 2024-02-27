"""
桶排序 - 

Author: kayotin
Date 2024/2/27
"""


def bucket_sort(nums: list[float]):
    """桶排序"""
    # 初始化 k = n/2 个桶，预期向每个桶分配 2 个元素
    k = len(nums) // 2
    buckets = [[] for _ in range(k)]
    # 1，将数组元素分配到各个桶中
    for num in nums:
        # 输入数据范围为[0,1),使用num*k映射到索引范围[0, k-1]
        # 因为num的值是小于1的，所以num*k 始终在 [0, k-1] 范围内
        i = int(num * k)
        buckets[i].append(num)
    # 2.对各个桶执行排序
    for bucket in buckets:
        bucket.sort()
    # 3.遍历桶合并结果
    i = 0
    for bucket in buckets:
        for num in bucket:
            nums[i] = num
            i += 1
