"""
47_二进制中1的个数 - 

Author: hanayo
Date： 2024/4/14
"""


def one_count(num: int):
    num_bin = str(bin(num))[2:]
    count = 0
    for s in num_bin:
        if s == "1":
            count += 1
    print(count)


while True:
    try:
        my_num = int(input())
        one_count(my_num)
    except EOFError:
        break
