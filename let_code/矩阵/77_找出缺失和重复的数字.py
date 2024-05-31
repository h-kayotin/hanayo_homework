"""
77_找出缺失和重复的数字 - 

Author: hanayo
Date： 2024/5/31
"""
import math
from typing import List


def find_values(grid: List[List[int]]) -> List[int]:
    """傻傻遍历"""
    count_dict = dict()
    res = []
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] not in count_dict.keys():
                count_dict[grid[i][j]] = 1
            else:
                res.append(grid[i][j])

    num_list = list(count_dict.keys())
    num_list.sort()
    st_num = 0
    for i in range(len(num_list)):
        st_num += 1
        if num_list[i] != st_num:
            res.append(num_list[i] - 1)
            break
    if len(res) == 1:
        res.append(n * n)
    return res


def find_values2(grid: List[List[int]]) -> List[int]:
    """用数组记录，用列表的index方法"""
    n = len(grid)
    count = [0] * (n*n+1)
    count[0] = -1
    for i in range(n):
        for j in range(n):
            count[grid[i][j]] += 1
    return [count.index(2), count.index(0)]


if __name__ == '__main__':
    find_values([[9,1,7],[8,9,2],[3,4,6]])