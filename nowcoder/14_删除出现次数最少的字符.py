"""
14_删除出现次数最少的字符 - 描述
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

数据范围：输入的字符串长度满足 1≤n≤20  ，保证输入的字符串中仅出现小写字母

Author: hanayo
Date： 2024/3/22
"""


def check_str(my_str: str):
    for s in my_str:
        if s in str_dict:
            str_dict[s] += 1
        else:
            str_dict[s] = 1

    val_tuples = str_dict.items()
    min_s, min_v = min(val_tuples,  key=lambda x: x[1])

    del_list = list()
    for key, val in val_tuples:
        if val == min_v:
            del_list.append(key)
    new_str = my_str
    for c in del_list:
        new_str = new_str.replace(c, "")
    print(new_str)


str_dict = dict()
my_s = input()
check_str(my_s)