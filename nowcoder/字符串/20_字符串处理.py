"""
20_字符串处理 - 

Author: kayotin
Date 2024/3/24
"""

input_val = str(input())
str1, str2 = input_val.split(" ")

my_str = str1 + str2
list1, list2 = [], []
for i in range(len(my_str)):
    if i%2:
        list1.append(my_str[i])
    else:
        list2.append(my_str[i])

list1.sort()
list2.sort()
itr1 = iter(list1)
itr2 = iter(list2)


res = ""
cur = 0
for i in range(len(my_str)):
    if cur:
        try:
            res += next(itr1)
            cur = 0
        except StopIteration:
            pass
    else:
        try:
            res += next(itr2)
            cur = 1
        except StopIteration:
            pass


def turn_off(c: str):
    if c.isdigit():
        c_bin = str(bin(int(c)))[2:].zfill(4)
        new_bin = c_bin[::-1]
        new_num = int(new_bin, 2)
        if new_num < 10:
            return str(new_num)
        else:
            return str(hex(new_num))[2:].upper()
    else:
        try:
            # 先转10进制
            new_num = int(c.lower(), 16)
            # 10进制转2进制代码
            new_code = str(bin(new_num))[2:].zfill(4)
            turn_code = new_code[::-1]
            new_num = int(turn_code, 2)
            if new_num < 10:
                return str(new_num)
            else:
                return str(hex(new_num))[2:].upper()
        except ValueError:
            return c


final = ""
for n_c in res:
    new_c = turn_off(n_c)
    final += new_c

print(final)