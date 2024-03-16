"""
15_最长子串 - 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。

Author: kayotin
Date 2024/3/16
"""


def len_of_substring(s: str):
    # 该字典用来记录字母出现的位置
    dic = dict()
    res = 0
    i = -1
    for j in range(len(s)):
        # 如果某个字母出现过，就更新i的位置
        if s[j] in dic:
            i = max(i, dic[s[j]])
        dic[s[j]] = j
        res = max(res, j-i)
    return res


if __name__ == '__main__':
    my_s = "abcabcbb"
    print(len_of_substring(my_s))
