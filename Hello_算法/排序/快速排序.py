"""
快速排序 - 

Author: kayotin
Date 2024/2/22
"""


def partition(nums: list[int], left: int, right: int) -> int:
    """哨兵划分"""
    # 以 nums[left] 为基准数
    i, j = left, right
    while i < j:
        # 从右向左，找首个小于基准数的数字
        while i < j and nums[j] >= nums[left]:
            j -= 1
        # 从左到右，找首个大于基准数的数字
        while i < j and nums[i] <= nums[left]:
            i += 1
        # 交换这两个数字
        nums[i], nums[j] = nums[j], nums[i]
    # 将基准数交换至边界
    nums[i], nums[left] = nums[left], nums[i]
    return i


def quick_sort(nums: list[int], left: int, right: int):
    """快速排序"""
    # 子数组长度为 1 时终止递归
    if left >= right:
        return
    # 哨兵划分
    pivot = partition(nums, left, right)
    # 递归左子数组、右子数组
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)


def median_three(nums: list[int], left: int, mid: int, right: int) -> int:
    """选取三个候选元素的中位数"""
    # 此处使用异或运算来简化代码
    # 异或规则为 0 ^ 0 = 1 ^ 1 = 0, 0 ^ 1 = 1 ^ 0 = 1
    if (nums[left] < nums[mid]) ^ (nums[left] < nums[right]):
        return left
    elif (nums[mid] < nums[left]) ^ (nums[mid] < nums[right]):
        return mid
    else:
        return right


def partition2(nums: list[int], left: int, right: int) -> int:
    """哨兵划分（三数取中值）"""
    # 以 nums[left] 为基准数
    med = median_three(nums, left, (left + right) // 2, right)
    # 将中位数交换至数组最左端
    nums[left], nums[med] = nums[med], nums[left]
    # 以 nums[left] 为基准数
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1  # 从右向左找首个小于基准数的元素
        while i < j and nums[i] <= nums[left]:
            i += 1  # 从左向右找首个大于基准数的元素
        # 元素交换
        nums[i], nums[j] = nums[j], nums[i]
    # 将基准数交换至两子数组的分界线
    nums[i], nums[left] = nums[left], nums[i]
    return i  # 返回基准数的索引


def quick_sort2(self, nums: list[int], left: int, right: int):
    """快速排序（尾递归优化）"""
    # 子数组长度为 1 时终止
    while left < right:
        # 哨兵划分操作
        pivot = self.partition(nums, left, right)
        # 对两个子数组中较短的那个执行快速排序
        if pivot - left < right - pivot:
            self.quick_sort(nums, left, pivot - 1)  # 递归排序左子数组
            left = pivot + 1  # 剩余未排序区间为 [pivot + 1, right]
        else:
            self.quick_sort(nums, pivot + 1, right)  # 递归排序右子数组
            right = pivot - 1  # 剩余未排序区间为 [left, pivot - 1]


if __name__ == '__main__':
    my_nums = [2, 4, 1, 0, 3, 5]
    quick_sort(my_nums, 0, len(my_nums) - 1)
    print(my_nums)