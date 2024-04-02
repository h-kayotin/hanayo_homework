"""
32_字符统计 - 

统计字符的英文字母、空格、数字和其他字符个数
Author: hanayo
Date： 2024/4/2
"""


def count_str(my_str: str):
    res = [0] * 4
    for c in my_str:
        if c.isalpha():
            res[0] += 1
        elif ord(c) == ord(" "):
            res[1] += 1
        elif c.isdigit():
            res[2] += 1
        else:
            res[3] += 1
    for r in res:
        print(r)
