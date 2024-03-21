"""
10_识别有效IP地址 - 

Author: hanayo
Date： 2024/3/21
"""

# ABCDE 无效，私人地址
ip_dict = {
    "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "Error": 0, "Private": 0
}


def get_bit(ip, n):
    """从ip中获得第几位"""
    bit_list = ip.split(".")
    bit = int(bit_list[n])
    return bit


def check_ip(ip: str):
    bit_list = ip.split(".")
    if len(bit_list) != 4:
        return False
    for bit in bit_list:
        try:
            bit = int(bit)
            if bit > 255 or bit < 0:
                return False
        except ValueError:
            return False
    return True


def check_type(ip: str):
    bit1 = get_bit(ip, 0)
    if bit1 == 0:
        return None
    elif bit1 <= 126:
        return "A"
    elif bit1 == 127:
        return None
    elif bit1 <= 191:
        return "B"
    elif bit1 <= 223:
        return "C"
    elif bit1 <= 239:
        return "D"
    else:
        return "E"


def check_private(ip: str):
    bit1 = get_bit(ip, 0)
    if bit1 == 10:
        return True
    bit2 = get_bit(ip, 1)
    if bit1 == 172 and 16 <= bit2 <= 31:
        return True
    if bit1 == 192 and bit2 == 168:
        return True
    return False


def check_mask(mask: str):
    if not check_ip(mask):
        return False
    if mask in {"0.0.0.0", "255.255.255.255"}:
        return False
    bit_list = mask.split(".")
    res = ""
    for bit in bit_list:
        bit_num = bin(int(bit))[2:]
        res += str(bit_num.zfill(8))
    # 从左往右，找第一个0
    zero_i = res.find("0")
    # 从右往左，找第一个1
    one_i = res.rfind("1")
    if zero_i - one_i == 1:
        return True
    else:
        return False


def main():
    while True:
        ip, mask = str(input()).split("~")
        bit1 = get_bit(ip, 0)
        # 这一步一定要有，否则本该跳过的，会计入错误地址中
        if bit1 == 127 or bit1 == 0:
            continue
        if check_ip(ip) and check_mask(mask):
            ip_type = check_type(ip)
            if ip_type:
                ip_dict[ip_type] += 1
            if check_private(ip):
                ip_dict['Private'] += 1
        else:
            ip_dict['Error'] += 1


if __name__ == '__main__':
    try:
        main()
    except (EOFError, ValueError):
        pass
    for key in ip_dict.keys():
        print(ip_dict[key], end=" ")
