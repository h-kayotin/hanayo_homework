"""
15_合唱队问题 - 中间最高，左侧递增，右侧递减，这就是一个合格的合唱队
输入描述：
用例两行数据，第一行是同学的总数 N ，第二行是 N 位同学的身高，以空格隔开

输出描述：
最少需要几位同学出列
Author: hanayo
Date： 2024/3/22
"""


def find_max_add(nums):
    """寻找最长递增序列"""
    for i in range(1, len(nums)):
        for j in range(i+1, len(nums)):
            pass


def main():
    team_len = int(input())
    if team_len == 1:
        return 0
    heights_str = str(input())
    h_list = [int(x) for x in heights_str.split(" ")]
    max_h = max(h_list)
    max_index = 0
    for h in h_list:
        max_index += 1
        if h == max_h:
            break
    print(max_index)
    left_list = h_list[0: max_index]
    right_light = h_list[max_index:]


if __name__ == '__main__':
    main()