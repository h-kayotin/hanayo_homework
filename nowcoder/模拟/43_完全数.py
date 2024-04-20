"""
43_完全数 -

完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。

它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。

例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。

输入n，请输出n以内(含n)完全数的个数。

Author: hanayo
Date： 2024/4/9
"""
from math import sqrt


def is_perfect_num(n):

    res = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            res.append(i)
            res.append(int(n/i))
    if sum(res) == n:
        return True
    else:
        return False


num = int(input())
res = 0
for i in range(3, num):
    if is_perfect_num(i):
        res += 1
print(res)