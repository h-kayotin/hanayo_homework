"""
06_统计二进制1的个数 - 

Author: kayotin
Date 2024/3/19
"""

num = 10
bin_num = bin(num)
str_num = str(bin_num)[2:]
count = 0
for i in range(len(str_num)):
    if str_num[i] == "1":
        count += 1
print(count)
