"""
25_整数和ip地址转换 - 
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
Author: kayotin
Date 2024/3/31
"""


def ip_to_int(ip:str):
    nums = [int(x) for x in ip.split(".")]
    res = ""
    for num in nums:
        code = str(bin(num))[2:]
        res += code.zfill(8)
    print(int(res, 2))


def int_to_ip(num:int):
    code = str(bin(num))[2:].zfill(32)
    ip = ""
    for i in range(4):
        ip_bin = str(code[i*8: i*8+8])
        int_num = int(ip_bin, 2)
        ip += f"{int_num}."
    print(ip[:-1])


# ip_to_int("10.0.3.193")
int_to_ip(167969729)
