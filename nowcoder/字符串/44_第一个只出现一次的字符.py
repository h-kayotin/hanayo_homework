"""
44_字符串中第一个只出现一次的字符 - 

Author: kayotin
Date 2024/4/11
"""


def first_s(my_s: str):
    res_dict = {}
    for i in range(len(my_s)):
        if my_s[i] not in res_dict:
            res_dict[my_s[i]] = [1, i]
        else:
            res_dict[my_s[i]][0] += 1

    res = []
    for key in res_dict:
        if res_dict[key][0] == 1:
            res.append(res_dict[key][1])
    if not res:
        return -1
    return my_s[min(res)]