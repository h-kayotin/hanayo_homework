"""
48_光标位置 - 

Author: hanayo
Date： 2024/4/14
"""


def mp3_location(song_num: int, op: str):
    num_list = [x for x in range(1, song_num + 1)]
    cur_idx = 0
    window = num_list[:4]

