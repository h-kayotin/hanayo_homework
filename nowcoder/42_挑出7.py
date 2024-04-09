"""
42_挑出7 - 
输出 1到n之间 的与 7 有关数字的个数。
一个数与7有关是指这个数是 7 的倍数，或者是包含 7 的数字（如 17 ，27 ，37 ... 70 ，71 ，72 ，73...）
Author: hanayo
Date： 2024/4/9
"""


def get_seven(n):
    """强行遍历法"""
    count = 0
    if n < 7:
        return 0
    for i in range(7, n+1):
        if i % 7 == 0:
            count += 1
            continue
        if "7" in str(i):
            count += 1
    print(count)


get_seven(20)
