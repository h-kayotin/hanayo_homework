"""
no_04 - 有序数组合并

Author: kayotin
Date 2024/1/30
"""

nums1 = [1, 3, 5, 7]
n = len(nums1)
nums2 = [2, 4, 6, 7, 8]
m = len(nums2)

i = j = 0
nums_res = list()
while i < n and j < m:
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
print("i", i)
print("j", j)
if j < m:
    nums_res.extend(nums2[j:])
elif i < n:
    nums_res.extend(nums1[j:])

print(nums_res)
