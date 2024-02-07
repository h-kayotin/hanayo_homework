"""
字符串拼接 - 

Author: kayotin
Date 2024/2/4
"""

import os.path

# > 向右对齐 < 向左对齐
a = '{:>20}'.format('contents')
b = '{:<20}'.format('contents')
print(a)
print(b)
# 居中，并用-填充
print('{:-^20}'.format('contents'))


def my_title(text, padding='-', width =20):
    """自定义函数处理超过20字符的时候"""
    return '{1}{0:{1}^{2}}{1}'.format(text, padding, width-2)


print(my_title('This is a long holiday~~'))
print(my_title('contents'))