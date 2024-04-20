"""
29_兔子数量 - 
有一种兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子。
计算第n个月的兔子总数
Author: kayotin
Date 2024/3/31
"""


def count_rabbits(month: int):
    rabbits = [0]
    for i in range(month):
        for j in range(len(rabbits)):
            rabbits[j] += 1
            if rabbits[j] >= 3:
                rabbits.append(1)

    print(len(rabbits))


if __name__ == '__main__':
    count_rabbits(31)