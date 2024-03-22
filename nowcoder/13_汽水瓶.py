"""
13_汽水瓶 - 某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
数据范围：输入的正整数满足 1≤n≤100
输入：
3
10
81
0

输出：
1
5
40

说明：
样例 1 解释：用三个空瓶换一瓶汽水，剩一个空瓶无法继续交换
样例 2 解释：用九个空瓶换三瓶汽水，剩四个空瓶再用三个空瓶换一瓶汽水，剩两个空瓶，向老板借一个空瓶再用三个空瓶换一瓶汽水喝完得一个空瓶还给老板
Author: hanayo
Date： 2024/3/22
"""

exp_list = list()


def input_val():
    while True:
        num = int(input())
        if num:
            exp_list.append(num)
        else:
            break


def check_bots(bot_num: int):
    # 和到的汽水
    res_bot = 0
    # 当前手上的空瓶
    cur_bot = bot_num
    while True:
        # 本轮换到的汽水
        bot = cur_bot // 3
        res_bot += bot
        # 换完后，手上当前汽水
        cur_bot -= bot * 3  # 失去3x的空瓶
        cur_bot += bot  # 得到x新的空瓶
        if cur_bot < 3:
            break
    # 计算最终情况
    if cur_bot == 2:
        res_bot += 1
    print(res_bot)


if __name__ == '__main__':
    input_val()
    for exp in exp_list:
        check_bots(exp)
