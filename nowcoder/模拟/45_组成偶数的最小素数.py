"""
45_组成偶数的最小素数 - 
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。
Author: kayotin
Date 2024/4/12
"""
from math import sqrt


def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def find_min_prime(n):
    num = int(n/2)
    for i in range(num, 1, -1):
        if is_prime(i) and is_prime(n-i):
            return i


print(find_min_prime(20))
