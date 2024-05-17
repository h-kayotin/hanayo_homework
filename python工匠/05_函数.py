"""
05_函数 - 

Author: hanayo
Date： 2024/5/17
"""
import functools


# 函数最好只返回一种结果

# 使用偏函数改写函数
def multiply(x, y):
    return x * y


# def double(value):
#     # 返回另一个函数调用结果
#     return multiply(2, value)
# 偏函数，可以固定其中一些参数
double = functools.partial(multiply, 2)
print(double(4))