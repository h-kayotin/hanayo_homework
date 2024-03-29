"""
04_最大切分乘积问题 - 

Author: hanayo
Date： 2024/3/29
"""
import math


def max_product_cutting(n: int) -> int:
    """最大切分乘积：贪心"""
    # 当 n <= 3 时，必须切分出一个 1
    if n <= 3:
        return 1*(n-1)
    # 贪心地切分出 3 ，a 为 3 的个数，b 为余数
    a, b = n // 3, n % 3
    # 余数为1
    if b == 1:
        return int(math.pow(3, a-1)) * 2 * 2
    # 余数为2
    if b == 2:
        return int(math.pow(3, a)) * 2
    # 余数为3，不做处理
    return int(math.pow(3, a))
