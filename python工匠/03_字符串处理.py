"""
03_字符串处理 - 

Author: hanayo
Date： 2024/5/16
"""
from math import inf

# 比较大的数字可以用_来分隔，便于阅读
print(10_000_000.0)
print(type(10_000_000.0))
print(int('0b_1111_0000', 2))  # 处理字符串的时候也会正确处理下划线

# 使用rsplit或者rstrip()
log_line = '"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" 47632'
print(log_line.rsplit(None, 1))

# 使用“无穷大” float("inf")
# A. 根据年龄升序排序，没有提供年龄放在最后边
users = {"tom": 19, "jenny": 13, "jack": None, "andrew": 43}
sort_users = sorted(users.keys(), key=lambda x: users.get(x) or inf)
print(sort_users)
# 作为循环的初始值
max_num = -inf
for num in [1, 2, 3, 4]:
    max_num = max(max_num, num)

# 常见误区
# val += 1 并不是线程安全的
# 字符串的拼接并不慢，可以放心使用
print(",".join(['1', '2', '3']))
