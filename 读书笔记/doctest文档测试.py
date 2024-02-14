"""
doctest - 

Author: kayotin
Date 2024/2/14
"""


def add_numbers(a, b):
    """
    计算两个数的和

    >>> add_numbers(3, 5)
    8
    >>> add_numbers(7, 9)
    15
    """
    return a + b


if __name__ == "__main__":
    # 执行 doctest 测试
    import doctest
    doctest.testmod()
