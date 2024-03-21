"""
09_坐标输入输出 - 

Author: hanayo
Date： 2024/3/21
"""

move_dict = {"A": (-1, 0), "W": (0, 1), "S": (0, -1), "D": (1, 0)}


def input_value():
    """坐标输入"""
    src_val = str(input())
    # src_val = "A10;S20;W10;D30;X;A1A;B10A11;;A10;"
    res = []
    val_list = src_val.split(";")
    for val in val_list:
        # 过滤无效值，显然长度只能是2或者3
        if len(val) not in {2, 3}:
            continue
        direct = val[0]
        # 方向不在wasd中
        if direct not in move_dict.keys():
            continue
        try:
            num = int(val[1:])
            if num == 0:
                continue
            res.append((direct, num))
        except ValueError:
            continue
    return res


def get_val(val_tup: tuple):
    """计算前进的值"""
    direct, val = val_tup
    return move_dict[direct][0] * val, move_dict[direct][1] * val


def main():
    x0, y0 = 0, 0
    commands = input_value()
    for command in commands:
        x, y = get_val(command)
        x0 += x
        y0 += y
    return x0, y0


if __name__ == '__main__':
    res_tup = main()
    print(f"{res_tup[0]},{res_tup[1]}")
