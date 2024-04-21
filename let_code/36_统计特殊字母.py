"""
36_统计特殊字母 - 


给你一个字符串 word。如果 word 中同时出现某个字母 c 的小写形式和大写形式，
并且 每个 小写形式的 c 都出现在第一个大写形式的 c 之前，则称字母 c 是一个 特殊字母 。
Author: kayotin
Date 2024/4/21
"""


def number_special(word: str):
    upper_list = [0] * 26
    lower_list = [0] * 26
    for c in word:
        if c.isupper():
            upper_list[ord(c)-65] = 1
        else:
            lower_list[ord(c)-97] = 1

    count = 0
    for i in range(26):
        if upper_list[i] and lower_list[i]:
            count += 1
    return count


def number_special2(word: str):
    upper_list = [[0, 0] for _ in range(26)]
    lower_list = [[0, 0] for _ in range(26)]

    idx = 0
    for c in word:
        if c.isupper():
            if upper_list[ord(c)-65][0] == 1:
                upper_list[ord(c) - 65][1] = min(upper_list[ord(c) - 65][1], idx)
            else:
                upper_list[ord(c)-65][0] = 1
                upper_list[ord(c)-65][1] = idx
        else:
            lower_list[ord(c)-97][0] = 1
            lower_list[ord(c) - 97][1] = max(lower_list[ord(c) - 97][1], idx)

        idx += 1

    count = 0
    for i in range(26):
        if upper_list[i][0] and lower_list[i][0] and upper_list[i][1] > lower_list[i][1]:
            count += 1
    return count


number_special2("aaAbcBC")

