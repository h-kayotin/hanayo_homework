"""
48_光标位置 - 
模拟mp3歌曲显示，最多显示4首歌

输入描述：
输入说明：
1 输入歌曲数量
2 输入命令 U或者D

输出描述：
输出说明
1 输出当前列表
2 输出当前选中歌曲

Author: hanayo
Date： 2024/4/14
"""


def move_up(window: list[int], cur_idx: int, song_num, num_list):
    cur_idx -= 1
    # 第一首歌，往上翻页的情况
    if cur_idx < 0:
        cur_idx = song_num - 1
        cur_window = num_list[-4:]
    # 否则是正常翻页
    else:
        if cur_idx in window:
            cur_window = window
        else:
            cur_window = num_list[cur_idx:cur_idx+4]
    return cur_idx, cur_window


def move_down(window: list[int], cur_idx: int, song_num, num_list):
    cur_idx += 1
    # 最后一首歌，往下翻页的情况
    if cur_idx > song_num - 1:
        cur_idx = 0
        cur_window = num_list[:4]
    # 正常往下翻页
    else:
        if cur_idx in window:
            cur_window = window
        else:
            cur_window = num_list[cur_idx -3: cur_idx + 1]
    return cur_idx, cur_window


def mp3_location(song_num: int, op: str):
    num_list = [x for x in range(song_num)]
    cur_idx = 0
    cur_window = num_list[:4]
    for s in op:
        if s == "U":
            cur_idx, cur_window = move_up(cur_window, cur_idx, song_num, num_list)
        else:
            cur_idx, cur_window = move_down(cur_window, cur_idx, song_num, num_list)
    for song in cur_window:
        print(song + 1, end=" ")
    print()
    print(cur_idx +1)


# 输入的指令有简化的可能。
my_str = "UUUDD"
new_s = my_str[0]
for i in range(1, len(my_str)):
    if my_str[i] == new_s[-1]:
        new_s += my_str[i]
    else:
        new_s = new_s[:-1]
print(new_s)
