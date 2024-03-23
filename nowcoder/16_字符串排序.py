"""
16_字符串排序 - 
sorted(new_s, key=str.upper) 可以保持如果大小写都存在，按原始顺序
Author: kayotin
Date 2024/3/23
"""


def sort_str(my_str:str):

    new_s = ""
    for s in my_str:
        if s.isalpha():
            new_s += s

    new_sorted = sorted(new_s, key=str.upper)
    res = ""
    index = 0
    for i in range(len(my_str)):
        if my_str[i].isalpha():
            res += new_sorted[index]
            index += 1
        else:
            res += my_str[i]
    print(res)

if __name__ == '__main__':
    sort_str(str(input()))

