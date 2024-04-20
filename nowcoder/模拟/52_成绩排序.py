"""
52_成绩排序 - 

Author: hanayo
Date： 2024/4/19
"""


n = 3
sort_type = 0


my_list = [("jack", 70), ("peter", 96), ("Tom", 70), ("smith", 67)]

my_list.sort(key=lambda x:x[1], reverse=True)
print(my_list)

num_len = int(input())
sort_t = False if int(input()) else True
num_list = []
for _ in range(num_len):
    x1, x2 = str(input()).split(" ")
    num_list.append((x1, int(x2)))
num_list.sort(key=lambda x: x[1], reverse=sort_t)

for tup in num_list:
    print(f"{tup[0]} {tup[1]}")