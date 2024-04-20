"""
51_24点游戏 - 
给出4个1-10的数字，通过加减乘除运算，得到数字为24就算胜利,除法指实数除法运算,运算符仅允许出现在两个数字之间,本题对数字选取顺序无要求，但每个数字仅允许使用一次，且需考虑括号运算
此题允许数字重复，如3 3 4 4为合法输入，此输入一共有两个3，但是每个数字只允许使用一次，则运算过程中两个3都被选取并进行对应的计算操作。
Author: hanayo
Date： 2024/4/15
"""


def twentyfour_game(nums: list[int], item):
    if item < 1:
        return False
    # 递归终点，数组中只剩一个数字时
    if len(nums) == 1:
        return nums[0] == item
    else:
        # 遍历每个元素，分别尝试4种运算
        for i in range(len(nums)):
            m = nums[0:i] + nums[i+1:]
            n = nums[i]
            if twentyfour_game(m, item + n) or twentyfour_game(m, item - n) or twentyfour_game(m, item * n) \
                    or twentyfour_game(m, item/n):
                return True
        return False


