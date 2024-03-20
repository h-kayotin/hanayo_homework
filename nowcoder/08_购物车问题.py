"""
08_购物车问题 - 总预算1000，最多购买n件商品，商品的价值是 价格*重要性，并且
某些商品需要购买前置物品后才可以购买

Author: hanayo
Date： 2024/3/20
"""


class Good:
    def __init__(self, price, point, q):
        self.price = price
        self.val = price*point
        self.q = q

    def __str__(self):
        return f"{self.price} {self.val} {self.q}"


def get_value(price, point):
    """计算价格和满意度"""
    value_ = [price, price*point]
    return value_


def work(key, value, attachments):
    """模拟4种情况"""
    prices, points = [], []
    # 1.仅有主件
    prices.append(value[0])
    points.append(value[1])
    if key in attachments:
        # 2. 主件 + 附件1
        prices.append(prices[0] + attachments[key][0][0])
        points.append(points[0] + attachments[key][0][1])
        if len(attachments[key]) == 2:
            # 3.主件+附件2
            prices.append(prices[0] + attachments[key][1][0])
            points.append(prices[0] + attachments[key][1][1])
            # 4.主件+ 附件1 + 附件2
            prices.append(prices[0] + attachments[key][0][0] + attachments[key][1][0])
            points.append(points[0] + attachments[key][0][1] + attachments[key][1][1])
    return prices, points


def main():
    # 总预算1000， 可选商品5
    m, n = 1000, 5
    # 商品的价格 重要度 是否附件
    goods = [
        [800, 2, 0],
        [400, 5, 1],
        [300, 5, 1],
        [400, 3, 0],
        [500, 2, 0]
    ]
    # 主件 附件
    main_goods, attachments, res_list = {}, {}, [0] * (m+1)
    for i in range(n):
        price, point, att = goods[i][0], goods[i][1], goods[i][2]
        # 把商品简化成价格 和  满意度
        good = get_value(price, point)
        # 如果是主件
        if att == 0:
            # 添加进主件字典
            main_goods[i+1] = good
        # 如果是附件
        else:
            # 如果该附件编号key已经存在了
            if att in attachments:
                # 这个key下的列表，加上该附件商品
                attachments[att].append(good)
            # 不存在就创建这个key
            else:
                attachments[att] = [good]

    # 对主件字典进行遍历
    for key, value in main_goods.items():
        # prices列表和points列表，分别计算了4种情况的价格和满意度
        prices, points = work(key, value, attachments)
        # 对一列的所有值进行遍历
        for j in range(m, -1, -10):  # 价格是10的倍数
            # 判断价格是否在预算内
            for k in range(len(prices)):
                # 如果在预算内
                if j - prices[k] >= 0:
                    # 最优解在 上一次的最优解 和 剩余预算的最优解+当前满意度 之间取大的那个
                    res_list[j] = max(res_list[j], res_list[j-prices[k]] + points[k])
    print(res_list)
    return res_list[m]


if __name__ == '__main__':
    print(main())
