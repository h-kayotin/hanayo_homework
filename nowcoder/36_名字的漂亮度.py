"""
36_名字的漂亮度 - 
给出一个字符串，该字符串仅由小写字母组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。

给出多个字符串，计算每个字符串最大可能的“漂亮度”。
Author: kayotin
Date 2024/4/6
"""


def how_beauty(s: str):
    name_dict = dict()
    score = 26
    for c in s:
        if c not in name_dict.keys():
            name_dict[c] = 1
        else:
            name_dict[c] += 1
    res = list(name_dict.values())
    res.sort(reverse=True)
    beauty = 0
    for num in res:
        beauty += num * score
        score -= 1
    print(beauty)


n = int(input())
name_list = []
for i in range(n):
    how_beauty(str(input()))

how_beauty("lisi")