"""
12_简单密码 - 

Author: hanayo
Date： 2024/3/22
"""

str_dict = {
    "abc": 2, "def": 3, "ghi": 4, "jkl": 5, "mno": 6, "pqrs": 7, "tuv": 8, "wxyz": 9
}


def encrypt_pwd():
    pwd_str = str(input())
    res = ""
    for i in range(len(pwd_str)):
        if pwd_str[i].isdigit():
            res += pwd_str[i]
        elif pwd_str[i].islower():
            for key in str_dict.keys():
                if pwd_str[i] in key:
                    res += str(str_dict[key])
        else:
            if ord(pwd_str[i]) < 90:
                new_s_code = ord(pwd_str[i]) + 1
                res += chr(new_s_code).lower()
            else:
                res += "a"
    print(res)


encrypt_pwd()

