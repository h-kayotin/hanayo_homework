"""
109_划分字母区间 - 
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。

注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

返回一个表示每个字符串片段的长度的列表。
Author: hanayo
Date： 2024/7/1
"""
from typing import List


def partition_labels(self, s: str) -> List[int]:
    """这题目其实是要把字母分隔后，其他区间不含有该字母"""
    # 存储某个字母最后一次出现的index
    s_dict = {key: idx for idx, key in enumerate(s)}
    num = 0
    res = []
    # 第一个字符出现的最后位置
    j = s_dict[s[0]]

    for i in range(len(s)):
        num += 1
        if s_dict[s[i]] > j:
            j = s_dict[s[i]]
        if i == j:
            res.append(num)
            num = 0
    return res
