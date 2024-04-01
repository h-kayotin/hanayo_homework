"""
30_小球落地高度 - 

假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？

Author: hanayo
Date： 2024/4/1
"""


def ball_height(height: int):
    tot = 0
    for i in range(5):
        tot += height + height/2
        height = height/2
    print(tot - height)
    print(height)


ball_height(1)