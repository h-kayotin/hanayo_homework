"""
38_四则运算 - 

Author: kayotin
Date 2024/4/6
"""

my_str = "3+2*{1+2*[-4/(8-6)+7]}"
# maketrans生成转换表，translate方法执行转换
trans_str = my_str.translate(my_str.maketrans("{}[]", "()()"))
print(eval(trans_str))