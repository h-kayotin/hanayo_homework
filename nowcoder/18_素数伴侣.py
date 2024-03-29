"""
18_素数伴侣 - 
1.首先，只有奇数和偶数的和才能组成素数，所以分为奇数偶数来考虑
2.过程类似男女配对， 是一个递归的过程
    递的过程：如果一对男女已经配对， 新来的男的如果和女人合适，可以把之前的男人踢开，也和这个女人配对，让这个男的再去找别的对象
    归的过程：直到这个男人找不到对象，或不能往下踢了，一层层返回找对象的结果

Author: kayotin
Date 2024/3/23
"""
from math import sqrt


def is_prime(num: int):
    """判断是否是素数"""
    if num <= 1:
        return False
    if num <= 3:
        return True
    for i in range(2, int(sqrt(num))+2):
        if num % i == 0:
            return False
    return True


def teams_sp(nums: list[int]):
    odds, evens = [], []
    for num in nums:
        if num % 2:
            odds.append(num)
        else:
            evens.append(num)
    return odds, evens


def find(odd, vist, choose, evens):
    for j, even in enumerate(evens):
        # 这两个数可以匹配，并且没匹配过。把匹配状态记作True
        if is_prime(odd + even) and not vist[j]:
            vist[j] = True
            # 当前偶数没有配对的奇数，那么就把这奇数给它，返回True，or后面不再执行
            # 否则呢，就 让这个奇数，再去找新的伴侣
            if choose[j] == 0 or find(choose[j], vist, choose, evens):
                choose[j] = odd
                return True
    return False


def main():
    n = int(input())
    nums = str(input()).split(" ") 
    nums_list = [int(x) for x in nums]  
    odds, evens = teams_sp(nums_list)
    count = 0

    # 存放当前和这个偶数配对的奇数
    choose = [0] * len(evens)

    for odd in odds:
        # 存放是否当前奇数和偶数已经配对过
        vist = [False] * len(evens)
        if find(odd, vist, choose, evens):
            count += 1
    print(count)
        