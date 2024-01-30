"""
汽水瓶问题

https://www.nowcoder.com/exam/test/77331218/detail?pid=1088888
某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
数据范围：输入的正整数满足
1≤n≤100
"""


class DrinkNum:

    def __init__(self):
        self.nums_list = list()
        self.len = 0
        while True:
            if self.len >= 10:
                break
            input_num = int(input())
            if input_num:
                self.nums_list.append(input_num)
                self.len += 1
            else:
                break
        for bot_num in self.nums_list:
            print(check_bottom(bot_num))


def check_bottom(num):
    res_bot = 0
    now_bot = num
    while now_bot >= 3:
        # 表示这一轮换了几瓶
        this_bot = now_bot // 3
        # 表示最终多喝几瓶
        res_bot += this_bot
        # 表示当前剩余= 上一轮剩余 -
        now_bot = now_bot - 3*this_bot + this_bot
    if now_bot == 2:
        res_bot += 1
    return res_bot


DrinkNum()
