"""
19_字符串加密和解码 - 

Author: kayotin
Date 2024/3/23
"""


def encrypt_pwd(pwd_str: str):
    res = ""
    for c in pwd_str:
        if c.isdigit():
            res_num = int(c) + 1
            if res_num == 10:
                res_num = 0
            res += str(res_num)

        if c.islower():
            res_code = ord(c.upper())
            if res_code == ord("Z"):
                res_c = "A"
            else:
                res_c = chr(res_code + 1)
            res += res_c

        if c.isupper():
            res_code = ord(c.lower())
            if res_code == ord("z"):
                res_c = "a"
            else:
                res_c = chr(res_code + 1)

            res += res_c
    print(res)


def decrypt_pwd(pwd_str: str):
    res = ""
    for c in pwd_str:
        if c.isdigit():
            res_num = int(c) - 1
            if res_num == -1:
                res_num = 9
            res += str(res_num)

        if c.islower():
            res_code = ord(c.upper())
            if res_code == ord("A"):
                res_c = "Z"
            else:
                res_c = chr(res_code - 1)
            res += res_c

        if c.isupper():
            res_code = ord(c.lower())
            if res_code == ord("a"):
                res_c = "z"
            else:
                res_c = chr(res_code - 1)

            res += res_c
    print(res)


a = str(input())
b = str(input())
encrypt_pwd(a)
decrypt_pwd(b)