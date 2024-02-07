"""
字符串 - 

Author: kayotin
Date 2024/2/4
"""

# 普通字符串
print('I love you')

# 字节字符串
b_str = b'ever love'
print(b_str)

# 字节实际上就是数字，ord函数返回字节对应的数字 65
print(ord(b'A'))

# [101, 118, 101, 114, 32, 108, 111, 118, 101]
print(list(b_str))

# chr函数返回对应数字的字节
print(chr(65))