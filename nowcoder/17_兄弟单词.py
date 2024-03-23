"""
17_兄弟单词 - 

Author: kayotin
Date 2024/3/23
"""


def input_val():
    input_list = str(input()).split(" ")
    n = input_list[0]
    words_list = input_list[1:-2]
    target = input_list[-2]
    find_idx = int(input_list[-1])
    res_list = []
    for word in words_list:
        if word == target:
            continue
        if sorted(word) == sorted(target):
            res_list.append(word)
    res_list.sort()
    print(len(res_list))
    if find_idx < len(res_list):
        print(res_list[find_idx])



