"""
no_02_random_num - 随机数
生成了N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。


Author: kayotin
Date 2024/1/30
"""


class RandomNum:
    def __init__(self):
        self.num_len = int(input())
        self.num_list = list()
        for _ in range(self.num_len):
            self.num_list.append(int(input()))
        my_set = set(self.num_list)
        res_list = list(my_set)
        res_list.sort()
        for num in res_list:
            print(num)


if __name__ == '__main__':
    RandomNum()
