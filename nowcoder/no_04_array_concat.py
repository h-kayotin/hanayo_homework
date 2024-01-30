"""
no_04 - 有序数组合并

Author: kayotin
Date 2024/1/30
"""

nums1 = [1, 3, 5, 7]
n = len(nums1)
nums2 = [2, 4, 6, 8]
m = len(nums2)

i = j = 0
nums_res = list()
while True:
    if nums1[i] < nums2[j]:
        nums_res.append(nums1[i])
        i += 1
    elif nums1[i] > nums2[j]:
        nums_res.append(nums2[j])
        j += 1
    else:
        nums_res.append(nums1[i])
        nums_res.append(nums2[j])
        i += 1
        j += 1
    if i == len(nums1) - 1 and j < len(nums2) - 1:
        while j < len(nums2) - 1:
            nums_res.append(nums2[j])
        break
    elif j == len(nums2) - 1 and i < len(nums1) - 1:
        while i < len(nums1) - 1:
            nums_res.append(nums1[i])
        break
    elif i == len(nums1)-1 and j == len(nums2) - 1:
        break

print(nums_res)
