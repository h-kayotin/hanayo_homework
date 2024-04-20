"""
11_密码验证 - 

Author: hanayo
Date： 2024/3/22
"""

import sys


def pwd_is_ok(password: str):
    # 长度检验
    if len(password) < 8:
        return False
    # 类型是否大于4种的检验
    type_set = set()
    for s in password:
        if get_type(s):
            type_set.add(get_type(s))
        else:
            return False
    # print(type_set)
    if len(type_set) < 3:
        return False
    # 是否有大于2长度的重复子串
    n = len(password)
    # 存储子串的集合
    sub_set = set()
    for i in range(n):
        if i + 3 < n:
            sub_s = password[i: i+3]
            if sub_s in sub_set:
                return False
            sub_set.add(sub_s)
    return True


def get_type(s: str):
    if s.isdigit():
        return "num"
    elif s.isupper():
        return "upper"
    elif s.islower():
        return "lower"
    else:
        asc_code = ord(s)
        if asc_code == 32:
            return None
        return "sp"


res_list = list()


def main():
    while True:
        password = str(input())
        if not password:
            break
        if pwd_is_ok(password):
            res_list.append("OK")
        else:
            res_list.append("NG")


if __name__ == '__main__':
    main()
    for res in res_list:
        print(res)



