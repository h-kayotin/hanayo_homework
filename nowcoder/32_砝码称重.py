"""
32_砝码称重 - 

现有n种砝码，重量互不相等，分别为 m1,m2,m3…mn ；
每种砝码对应的数量为 x1,x2,x3...xn 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。

Author: hanayo
Date： 2024/4/2
"""


def max_weight(n, weights:list[int], amounts: list[int]):
    """穷举"""
    all_sub = []
    for i in range(n):
        # [重量]* 数量，得到每种砝码
        all_sub.extend([weights[i]] * amounts[i])

    res_set = {0}
    for ws in all_sub:
        # 每轮都和它相加取并集
        res_set = res_set.union({ws + res for res in res_set})

    print(len(res_set))


max_weight(2, [1,2], [2,1])
