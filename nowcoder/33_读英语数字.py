"""
33_读英语数字 - 

很没劲
Author: hanayo
Date： 2024/4/3
"""

eng_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}


def read_english(num: int):
    num_str = str(num)
    h_str = num_str[-3:]
    t_str = num_str[-6:-3]
    m_str = num_str[-9:-6]

    res = ""
    if m_str:
        m_int = int(m_str)
        res += f"{eng_dict[m_int]} million"
    if t_str:
        if int(t_str[0]):
            res += f"{eng_dict[int(t_str[0])]} hundred"
        if int(t_str[0]):
            res += f"{eng_dict[int(t_str[1])]} thousand"
        if int(t_str[0]):
            res += f"{eng_dict[int(t_str[2])]} thousand"

    print(res)

    print(m_str, t_str, h_str)


my_str = 1052510
read_english(my_str)
